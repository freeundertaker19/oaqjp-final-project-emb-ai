"""
Server module for the Emotion Detection application.
Provides routing interfaces using Flask to analyze customer feedback text
and display structural emotion score results.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask instance
app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emot_detector():
    """
    Retrieves query parameters from the frontend, executes emotion analysis,
    and formats the final output presentation layer message string.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # Check if the error handling payload was triggered (e.g., blank input)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is <b>{response['dominant_emotion']}</b>."
    )


@app.route("/")
def render_index_page():
    """
    Renders the default splash base landing page index.html interface template.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    