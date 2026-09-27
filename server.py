from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_endpoint():
    text_to_analyse = request.args.get("text")
    result = emotion_detector(text_to_analyse)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
