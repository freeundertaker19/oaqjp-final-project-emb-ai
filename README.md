# Repository for final project
Final Project

# Emotion Detection Web Application

An AI-infused Python web application deployed using Flask that leverages the Watson NLP Emotion Predict library. The application analyzes user feedback text statements and dynamically measures continuous score outputs for various primary emotional states.

## Project Structure
* **EmotionDetection/**: Core application module package logic.
* **static/**: Frontend presentation layer assets (JavaScript / CSS styles).
* **templates/**: Hypertext template structure files (`index.html`).
* **server.py**: Primary web routing orchestration application engine server.
* **test_emotion_detection.py**: Automation test harness execution unit script.

## Application Analysis Features
The application evaluates input feedback string contexts against five primary human emotion spectrum maps:
1. Anger
2. Disgust
3. Fear
4. Joy
5. Sadness

## Deployment Execution Instructions
To initialize the deployment instance server interface locally:
```bash
python3.11 server.py