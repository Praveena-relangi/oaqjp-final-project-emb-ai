import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analyzes the emotion of the given text using an external API.

    Parameters:
        text_to_analyze (str): The text to analyze.

    Returns:
        dict: A dictionary containing emotion scores and the dominant emotion, or an error message.
    """
    # Check if the input is blank
    if not text_to_analyze.strip():
        # Return a dictionary with None for all emotion keys if the input is blank
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Define the URL for the emotion analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = {"raw_document": {"text": text_to_analyze}}

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    try:
        response = requests.post(url, json=myobj, headers=header)
        if response.status_code == 200:
            data = response.json()
            emotion_dict = data['emotionPredictions'][0]['emotion']

            anger_score = emotion_dict.get('anger', 0)
            disgust_score = emotion_dict.get('disgust', 0)
            fear_score = emotion_dict.get('fear', 0)
            joy_score = emotion_dict.get('joy', 0)
            sadness_score = emotion_dict.get('sadness', 0)

            emotion_scores = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }
            
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            emotion_scores['dominant_emotion'] = dominant_emotion

            return emotion_scores

        elif response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

        else:
            # For other errors, return the status code and error message
            return {'error': f'Failed to get response from the API. Status code: {response.status_code}'}, 500

    except requests.exceptions.RequestException as e:
        # If there was an issue with the request (e.g., network error, invalid URL)
        return {'error': f'An error occurred while making the API request: {str(e)}'}, 500

    except KeyError as e:
        # If the response does not contain the expected keys
        return {'error': f'Unexpected response format. Missing key: {str(e)}'}, 500

    except Exception as e:
        # Catch any other unforeseen errors
        return {'error': f'An unexpected error occurred: {str(e)}'}, 500
