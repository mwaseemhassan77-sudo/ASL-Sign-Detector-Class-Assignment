import tkinter as tk
from tkinter import filedialog, Label, Button
from PIL import Image, ImageTk
import cv2
from asl_detector import ASLDetector
from utils import process_frame_for_display

class ASLApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ASL Alphabet Detector")
        self.root.geometry("600x500")
        self.detector = ASLDetector()
        self.cap = None

        # GUI elements
        self.label = Label(self.root, text="Upload an image or open camera for ASL detection")
        self.label.pack(pady=10)

        self.image_label = Label(self.root)
        self.image_label.pack()

        self.result_label = Label(self.root, text="", font=("Arial", 16))
        self.result_label.pack(pady=10)

        upload_btn = Button(self.root, text="Upload Image", command=self.upload_image)
        upload_btn.pack(pady=5)

        camera_btn = Button(self.root, text="Open Camera", command=self.open_camera)
        camera_btn.pack(pady=5)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])
        if file_path:
            image = Image.open(file_path).convert("RGB")
            pred_letter, pred_prob = self.detector.predict(image)
            self.display_image(image)
            self.result_label.config(text=f"Predicted: {pred_letter} ({pred_prob:.2f})")

    def display_image(self, pil_image, resize=(400, 300)):
        pil_image = pil_image.resize(resize)
        tk_image = ImageTk.PhotoImage(pil_image)
        self.image_label.config(image=tk_image)
        self.image_label.image = tk_image  # Keep reference

    def open_camera(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            self.result_label.config(text="Error: Could not open camera")
            return
        # Set lower resolution for faster processing
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.show_frame()

    def show_frame(self):
        if self.cap and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.flip(frame, 1)  # Mirror
                pil_image, pred_letter, pred_prob = process_frame_for_display(frame, self.detector)
                self.display_image(pil_image)
                self.result_label.config(text=f"Predicted: {pred_letter} ({pred_prob:.2f})")
            self.root.after(30, self.show_frame)  # 30ms ~33 FPS
        else:
            if self.cap:
                self.cap.release()

    def on_closing(self):
        if self.cap:
            self.cap.release()
        self.root.destroy()