
import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoModel


class SentryThreatDetector:

    def __init__(self, model_path, tokenizer_path):

        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu"
        )

        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(
            tokenizer_path
        )

        # Load pretrained DistilBERT
        self.model = AutoModel.from_pretrained(
            "distilbert-base-uncased"
        )

        # Classifier
        self.classifier = nn.Linear(768, 2)

        # Load trained classifier weights
        self.classifier.load_state_dict(
            torch.load(
                model_path,
                map_location=self.device
            )
        )

        self.model.to(self.device)
        self.classifier.to(self.device)

        self.model.eval()
        self.classifier.eval()


    def predict(self, text):

        encoded = self.tokenizer(
            text,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=64
        )

        encoded = {
            key: value.to(self.device)
            for key, value in encoded.items()
        }

        with torch.no_grad():

            output = self.model(**encoded)

            # First token = CLS representation
            cls_vector = output.last_hidden_state[:, 0, :]

            # Classifier
            logits = self.classifier(cls_vector)

            # Probabilities
            probabilities = torch.softmax(
                logits,
                dim=1
            )

            prediction = torch.argmax(
                probabilities,
                dim=1
            )

        predicted_class = prediction.item()

        if predicted_class == 0:
            label = "SAFE"
        else:
            label = "THREAT"

        confidence = probabilities[
            0, predicted_class
        ].item()

        return {
            "label": label,
            "confidence": confidence,
            "threat_probability": probabilities[0, 1].item(),
            "safe_probability": probabilities[0, 0].item()
        }
