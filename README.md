# Sentry — Threat Detection Model

A machine learning model developed for **Sentry**, an AI-powered personal safety system designed to identify potentially threatening language in real time.

## Overview

This model uses **Natural Language Processing (NLP)** to classify text into two categories:

* **THREAT** — language indicating a potential threat or dangerous situation
* **SAFE** — normal, non-threatening language

The model was trained on a **custom dataset created specifically for this project**.

## Machine Learning

The pipeline uses text preprocessing and machine learning techniques to learn patterns associated with threatening language rather than relying solely on manually programmed keywords or rules.

### Pipeline

```text
Input Text
    ↓
Text Preprocessing
    ↓
Feature Extraction
    ↓
Machine Learning Classifier
    ↓
THREAT / SAFE
```

## Example

```text
Input:
"My friend threatened to hurt me."

Prediction:
THREAT
```

```text
Input:
"I'm going home after work."

Prediction:
SAFE
```

## Model File

`threat_detection_model.pkl`

The `.pkl` file contains the trained machine learning model used for threat classification.

## Dataset

The training dataset was **manually created for this project** and contains labeled examples of threatening and non-threatening language.

No real personal conversations are used in the dataset.

## Purpose

This model serves as the **threat-understanding component of Sentry**. It can be integrated with Sentry's real-time audio/translation pipeline to analyze transcribed speech and identify potentially dangerous situations.

## Disclaimer

This model is a project prototype and should not be treated as a replacement for professional emergency services or human judgment.
