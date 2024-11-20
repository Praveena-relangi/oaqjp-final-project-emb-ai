"""This is the server module to run and route the requets."""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """Endpoint to render the index page."""
    return render_template('index.html')

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """
    Endpoint to analyze the emotion of the provided text.
    Expects a GET request with query parameter 'textToAnalyze'.
    """
    # Retrieve the text input from the query parameter
    text_to_analyze = request.args.get("textToAnalyze")

    # Check if the text input is empty or invalid
    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again."

    # Call the emotion_detector function with the provided text
    response = emotion_detector(text_to_analyze)

    # Check if the dominant emotion is None (invalid result)
    if response.get('dominant_emotion') is None:
        return "Invalid text! Please try again."

    # Format the response as per the requested format
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']}, "
        f"and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    return formatted_response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
