ASL Alphabet Sign Detector
This project detects American Sign Language (ASL) alphabet signs (A-Z) from images or live camera feed using a pretrained model from Hugging Face. It features a Tkinter-based GUI for user interaction.
Setup

Clone the repository:
git clone <your-repo-url>
cd asl_sign_detector


Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:
pip install -r requirements.txt


Run the application:
python src/main.py



Usage

Upload Image: Click "Upload Image" to select a JPG/PNG file of an ASL hand sign. The predicted letter and confidence score are displayed.
Open Camera: Click "Open Camera" for real-time detection. Position your hand clearly. Close the window to stop.
Requirements: A webcam for camera mode. Ensure good lighting and clear hand positioning for best results.

Project Structure

src/main.py: Entry point to launch the GUI.
src/asl_detector.py: Handles model loading and prediction.
src/gui.py: Tkinter GUI implementation.
src/utils.py: Utility functions for image processing and visualization.
requirements.txt: Lists dependencies.
README.md: This file.

Notes

Uses the pretrained model prithivMLmods/Alphabet-Sign-Language-Detection (~99.96% accuracy).
MediaPipe is used for optional hand landmark visualization.
Tested on Python 3.8+. Runs on CPU (GPU optional for faster inference).
For issues, ensure your camera is accessible and images are clear.

License
MIT License