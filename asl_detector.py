import os
from transformers import AutoImageProcessor, SiglipForImageClassification
import torch

# Suppress TensorFlow warnings
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

class ASLDetector:
    def __init__(self):
        self.model_name = "prithivMLmods/Alphabet-Sign-Language-Detection"
        self.processor = AutoImageProcessor.from_pretrained(self.model_name, use_fast=True)
        self.model = SiglipForImageClassification.from_pretrained(self.model_name)
        self.labels = {str(i): chr(65 + i) for i in range(26)}  # 0: 'A', 1: 'B', ..., 25: 'Z'

    def predict(self, image):
        """Predict ASL letter from a PIL Image."""
        inputs = self.processor(images=image, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            probs = torch.nn.functional.softmax(logits, dim=1).squeeze()
        top_idx = probs.argmax().item()
        top_prob = probs[top_idx].item()
        return self.labels[str(top_idx)], top_prob