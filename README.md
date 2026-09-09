
# Sentry Threat Language Detector

## Model

Base model:
distilbert-base-uncased

Task:
Threat language detection

## Classes

0 = SAFE
1 = THREAT

## Architecture

Text
↓
DistilBERT tokenizer
↓
DistilBERT
↓
CLS representation (768 dimensions)
↓
Linear classifier (768 → 2)
↓
SAFE / THREAT

## Training

DistilBERT was frozen during training.

Only the Linear(768, 2) classifier was trained.

Maximum sequence length:
64

## Files

sentry_threat_classifier.pth
    Trained classifier weights.

tokenizer/
    DistilBERT tokenizer files.

config.json
    Model configuration.

inference.py
    Python inference class.

## Example

from inference import SentryThreatDetector

detector = SentryThreatDetector(
    "sentry_threat_classifier.pth",
    "tokenizer"
)

result = detector.predict(
    "I'm going to hurt you"
)

print(result)

Expected output:

{
    "label": "THREAT",
    "confidence": ...,
    "threat_probability": ...,
    "safe_probability": ...
}
