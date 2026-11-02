''' Executing this function initiates the application of emotion
    detector to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, request, render_template

# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask(__name__)

@app.route("/emotionDetector")
def emo_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion detector over it using emotion_detector()
        function. The output returned shows the emotions and its scores 
        along with dominant emotion name.
    '''
    text_to_analyze = request.args.get('textToAnalyze').strip()
    result = emotion_detector(text_to_analyze)
    #check for blank response
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    formatted_response = f"'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}." # pylint: disable=line-too-long disable=trailing-whitespace
    return formatted_response
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')
if __name__ == "__main__":
    app()
