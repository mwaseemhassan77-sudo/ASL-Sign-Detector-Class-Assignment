import cv2
import mediapipe as mp
from PIL import Image
import numpy as np

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.3)


def process_frame_for_display(frame, detector):
    """Process a frame: predict ASL letter and draw landmarks."""
    # Downscale frame for faster processing
    frame = cv2.resize(frame, (320, 240))
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(image_rgb).convert("RGB")

    # Predict
    pred_letter, pred_prob = detector.predict(pil_image)

    # Draw landmarks and prediction
    result = hands.process(image_rgb)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                connection_drawing_spec=mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2)
            )
    cv2.putText(frame, f"{pred_letter} ({pred_prob:.2f})", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Convert back to PIL for Tkinter
    pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    return pil_image, pred_letter, pred_prob