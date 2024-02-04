import base64
import requests
import json

from config.loader import config, ConfigSchema

# Function to encode image to base64
def encode_image_to_base64(image_path):
    with open(image_path, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def make_identify_api_request(image_path):
    # API key
    api_key = config[ConfigSchema.PLANT_API_KEY]
    
    # Headers
    headers = {
        'Api-Key': api_key,
        'Content-Type': 'application/json'
    }
    
    # Encode the image
    encoded_image = encode_image_to_base64(image_path)
    
    # Data for the identification request
    identification_data = {
        'images': [f'data:image/jpg;base64,{encoded_image}'],
        'latitude': 49.207,
        'longitude': 16.608,
        'similar_images': True
    }

    # Make the identification request
    identification_response = requests.post(
        'https://plant.id/api/v3/identification',
        headers=headers,
        data=json.dumps(identification_data)
    )

    # Check identification response
    if identification_response.ok:
        return identification_response.json()
    else:
        return None

def make_health_api_request(image_path):
    # API key
    api_key = config[ConfigSchema.PLANT_API_KEY]
    
    # Headers
    headers = {
        'Api-Key': api_key,
        'Content-Type': 'application/json'
    }
    
    # Encode the image
    encoded_image = encode_image_to_base64(image_path)
    
    # Data for the health assessment request
    health_data = {
        'images': [f'data:image/jpg;base64,{encoded_image}'],
        'latitude': 49.207,
        'longitude': 16.608,
        'similar_images': True
    }
    
    # Make the health assessment request
    health_response = requests.post(
        'https://plant.id/api/v3/health_assessment',
        headers=headers,
        data=json.dumps(health_data)
    )

    # Check health assessment response
    if health_response.ok:
        return health_response.json()
    else:
        return None


def identify(image_path):
    identification_response = make_identify_api_request(image_path)
    if identification_response is None:
        return None
    else:
        best_match = identification_response['result']['classification']['suggestions'][0]
        similar_images = [pic['url'] for pic in best_match['similar_images']]
        result = {
            'name': best_match['name'],
            'probability': best_match['probability'],
            'images': similar_images
        }
        return json.dumps(result)

def health(image_path):
    health_response = make_health_api_request(image_path)
    if health_response is None:
        return None
    else:
        best_match = health_response['result']['disease']['suggestions'][0]
        similar_images = [pic['url'] for pic in best_match['similar_images']]
        result = {
            'is_healthy': health_response['result']['is_healthy']['probability'],
            'name': best_match['name'],
            'probability': best_match['probability'],
            'images': similar_images
        }
        return json.dumps(result)
