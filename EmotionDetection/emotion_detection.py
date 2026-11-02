'''Function to detect emotion from text.
The IBM watson NLP library will provide the result
'''
import requests
import json

#Function declaration for Emotion Detection. Takes text_to_analyze as string.
def emotion_detector(text_to_analyze):
    #API URL to fetch data from
    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    #Additional headers to send
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    #Prepare Input JSON
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    #call the API using requests module
    response = requests.post(URL, json=input_json, headers=headers)
    
    #return blank values for status code 400
    if response.status_code == 400:
        return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
                }

    #Covert response text to JSON object using json module
    response_json = json.loads(response.text)
    
    #Get score of all emotions from respose
    emotions = response_json["emotionPredictions"][0]["emotion"]    
    
    #Find dominant emotion name
    dominant_emotion = max(emotions, key=emotions.get)
    
    #Add dominant emotion name in emotions dict
    emotions["dominant_emotion"] = dominant_emotion
    
    return emotions
  
