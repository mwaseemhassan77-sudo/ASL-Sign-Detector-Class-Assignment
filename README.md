# 🤟 ASL Sign Detector

An AI-powered American Sign Language (ASL) Sign Detection system developed using Python, TensorFlow, OpenCV, and MediaPipe. This project recognizes ASL alphabet hand signs (A–Z) from uploaded images or real-time webcam input using a deep learning classification model.

The application provides a user-friendly GUI interface built with Tkinter and uses computer vision techniques for accurate hand gesture recognition. This project is designed for educational purposes, accessibility support, AI learning, and real-time sign language communication systems.

---

# 📌 Features

✅ Real-time ASL sign detection using webcam  
✅ Upload image prediction support  
✅ Deep Learning classification model  
✅ Hand landmark detection using MediaPipe  
✅ User-friendly Tkinter GUI  
✅ Confidence score prediction  
✅ Fast and accurate inference  
✅ AI-powered gesture recognition system  
✅ Supports ASL alphabet signs (A-Z)  
✅ Live camera detection mode  
✅ Image preprocessing and visualization utilities  

---

# 🧠 AI Model Information

This project uses a Deep Learning Classification Model trained to recognize ASL hand gestures.

The model predicts the correct alphabet sign based on hand shape and gesture patterns.

### Model Type
- Image Classification Model

### AI Technologies
- TensorFlow / Keras
- Computer Vision
- Deep Learning
- MediaPipe Hand Tracking

### Prediction Example

```text
Input Hand Sign → AI Model → Predicted Letter
```

Example:

```text
Hand Gesture → Prediction: "A" (98.7%)
```

---

# 📂 Dataset

This project uses the ASL Alphabet Dataset from Kaggle for training and testing.

## 🔗 Dataset Link

https://www.kaggle.com/datasets/ayuraj/asl-dataset?resource=download

### Dataset Includes
- ASL alphabet hand sign images
- Multiple gesture samples
- Different hand positions and angles
- Training-ready image structure

### Example Classes

```text
A
B
C
D
E
...
Z
```

---

# 🛠️ Technologies Used

## Programming Language
- Python

## Libraries & Frameworks
- TensorFlow
- Keras
- OpenCV
- MediaPipe
- NumPy
- Pillow
- Tkinter

## AI & Computer Vision
- Deep Learning
- Image Classification
- Hand Landmark Detection
- Real-Time Camera Processing

---

# 📥 Installation Guide

## 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd asl_sign_detector
```

---

## 2️⃣ Create Virtual Environment (Recommended)

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / Mac

```bash
python -m venv .venv
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
python src/main.py
```

---

# 💻 Application Usage

## 📸 Upload Image Mode

1. Open the application
2. Click **Upload Image**
3. Select a hand sign image
4. The AI model predicts the ASL alphabet
5. Confidence score is displayed

---

## 🎥 Live Camera Detection Mode

1. Click **Open Camera**
2. Show your hand sign in front of webcam
3. The model detects the gesture in real-time
4. Prediction appears instantly on screen

### Tips for Better Accuracy
- Use proper lighting
- Keep hand visible clearly
- Avoid background clutter
- Position hand properly in camera frame

---

# 📁 Project Structure

```text
asl_sign_detector/
│
├── src/
│   ├── main.py
│   ├── asl_detector.py
│   ├── gui.py
│   ├── utils.py
│   └── model/
│
├── dataset/
├── requirements.txt
├── README.md
└── assets/
```

---

# 📄 File Description

| File | Description |
|------|-------------|
| `main.py` | Main entry point of application |
| `asl_detector.py` | Loads AI model and predicts signs |
| `gui.py` | Tkinter graphical interface |
| `utils.py` | Image processing utilities |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

---

# 🔍 How It Works

The system follows these steps:

```text
Camera/Image Input
        ↓
Hand Detection (MediaPipe)
        ↓
Image Preprocessing
        ↓
TensorFlow Classification Model
        ↓
ASL Alphabet Prediction
        ↓
Display Result
```

---

# 🎯 Use Cases

- Sign Language Learning
- Accessibility Applications
- AI & Computer Vision Education
- Gesture Recognition Systems
- Human Computer Interaction
- Real-Time Communication Assistance

---

# ⚡ Performance

- Real-time detection support
- Lightweight GUI interface
- CPU compatible
- GPU acceleration optional
- Fast inference speed

---

# 📌 Requirements

## Software Requirements
- Python 3.10+
- Webcam (for live detection)

## Hardware Requirements
- Minimum 4GB RAM
- Recommended GPU for faster inference

---

# 🚀 Future Improvements

✅ Sentence recognition  
✅ Word prediction system  
✅ Voice output from hand signs  
✅ Mobile app integration  
✅ Multi-hand detection  
✅ Improved model accuracy  
✅ Custom gesture support  
✅ Real-time translation system  

---

# 🧪 Testing

The project has been tested with:
- Webcam live detection
- Uploaded image predictions
- Multiple hand positions
- Different lighting conditions

---

# 📌 Notes

- MediaPipe is used for hand landmark tracking
- OpenCV handles webcam processing
- TensorFlow powers the AI classification model
- GPU support improves performance significantly
- Best accuracy achieved with proper lighting

---

# 🛡️ License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

## Hassan CH

Software Engineer | Python AI Developer | Computer Vision Enthusiast

---

# ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.
