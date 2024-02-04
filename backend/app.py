from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from typing import Any, Tuple

from db.edit_listings import remove_listing, sell_from_listing
from db.login import is_valid_email, is_valid_password, login, signup
from db.get import get_fruits, get_listings, get_user_sales, get_vegetables
from db.post import create_new_sale
from plant_id.requests import identify, health, download_image, delete_temp_file

app = Flask(__name__)
CORS(app)

def is_not_none(*args: Tuple[Any]) -> bool:
    return all(arg is not None for arg in args)

@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.json
    
    # Validate email and password
    if not is_valid_email(data.get('email')) or not is_valid_password(data.get('password')):
        return jsonify({'status': -1, 'message': 'Invalid email or password format'}), 400
    
    status, user_info = login(data['email'], data['password'])
    return jsonify({'status': status, 'user_info': user_info})

@app.route('/api/signup', methods=['POST'])
def api_signup():
    data = request.json
    
    # Validate all fields
    if not (is_valid_email(data.get('email')) and is_valid_password(data.get('password'))
            and data.get('first_name') and data.get('last_name')):
        return jsonify({'status': -1, 'message': 'Invalid input'}), 400

    # Validate user input
    if not is_not_none(data['email'], data['password'], data['first_name'], data['last_name']):
        return jsonify({'status': -1, 'message': 'Invalid input'}), 400
    
    status = signup(data['email'], data['password'], data['first_name'], data['last_name'])
    return jsonify({'status': status})

@app.route('/api/get_user_sales', methods=['GET'])
def api_get_user_sales():
    email = request.args.get('email')
    if not is_valid_email(email):
        return jsonify({'status': -1, 'message': 'Invalid email format'}), 400
    status, sales = get_user_sales(email)
    return jsonify({'status': status, 'sales': sales})

# @app.route('/api/get_listings', methods=['GET'])
# def api_get_listings():
#     email = request.args.get('email')
#     if not is_valid_email(email):
#         return jsonify({'status': -1, 'message': 'Invalid email format'}), 400
#     status, listings = get_listings(email)
#     return jsonify({'status': status, 'listings': listings})

@app.route('/api/get_vegetables', methods=['GET'])
def api_get_vegetables():
    email = request.args.get('email')
    if not is_valid_email(email):
        return jsonify({'status': -1, 'message': 'Invalid email format'}), 400
    status, vegetables = get_vegetables(email)
    return jsonify({'status': status, 'vegetables': vegetables})

@app.route('/api/get_fruits', methods=['GET'])
def api_get_fruits():
    email = request.args.get('email')
    if not is_valid_email(email):
        return jsonify({'status': -1, 'message': 'Invalid email format'}), 400
    status, fruits = get_fruits(email)
    return jsonify({'status': status, 'fruits': fruits})

@app.route('/api/create_new_sale', methods=['POST'])
def api_create_new_sale():
    data = request.json
    # Validate email
    if not is_valid_email(data.get('email')):
        return jsonify({'status': -1, 'message': 'Invalid email format'}), 400
    
    # Validate user input
    if not is_not_none(data.get('email'), data.get('name'), data.get('description'), data.get('image'), data.get('is_fruit'), data.get('price'), data.get('quantity')):
        return jsonify({'status': -1, 'message': 'Invalid input'}), 400
    
    result = create_new_sale(data.get('email'), data.get('name'), data.get('description'), data.get('image'), data.get('is_fruit'), data.get('price'), data.get('quantity'))
    
    if result > 0:
        return jsonify({'status': result, 'message': 'Sale listing created successfully'}), 200
    elif result == -1:
        return jsonify({'status': -1, 'message': 'Email does not exist'}), 404
    else:
        return jsonify({'status': -2, 'message': 'An error occurred'}), 500

@app.route('/api/remove_listing', methods=['POST'])
def api_remove_listing():
    data = request.json
    result = remove_listing(data.get('email'), data.get('listing_id'))
    if result == 0:
        return jsonify({'status': 0, 'message': 'Listing removed successfully'}), 200
    elif result == -1:
        return jsonify({'status': -1, 'message': 'Email and listing ID do not match'}), 400
    else:
        return jsonify({'status': result, 'message': 'An error occurred'}), 500

@app.route('/api/sell_from_listing', methods=['POST'])
def api_sell_from_listing():
    data = request.json
    result = sell_from_listing(data.get('listing_id'), data.get('qty_sold'))
    if result >= 0:
        return jsonify({'status': 0, 'updated_quantity': result, 'message': 'Listing quantity updated successfully'}), 200
    elif result == -1:
        return jsonify({'status': -1, 'message': 'Listing does not exist'}), 400
    elif result == -2:
        return jsonify({'status': -2, 'message': 'Not enough quantity available'}), 400
    else:
        return jsonify({'status': result, 'message': 'An error occurred'}), 500

@app.route('/api/identify', methods=['POST'])
def api_identify():
    image_path = request.json.get('image_path')
    
    download_image(image_path, 'resources/tmp.jpg')
    image_path = 'resources/tmp.jpg'
    
    # Check if the path exists
    if not os.path.exists(image_path):
        return jsonify({'status': -1, 'message': 'File path does not exist'}), 400
    
    # Check if the file is in jpg or png format
    if not (image_path.endswith('.jpg') or image_path.endswith('.png')):
        return jsonify({'status': -2, 'message': 'File format must be JPG or PNG'}), 400
    
    # Call the identify function
    identification_result = identify(image_path)
    delete_temp_file(image_path)
    
    # Check the result
    if identification_result is None:
        return jsonify({'status': -3, 'message': 'Plant ID API call returned None'}), 500
    
    return jsonify({'status': 0, 'result': json.loads(identification_result)}), 200

@app.route('/api/health', methods=['POST'])
def api_health():
    image_path = request.json.get('image_path')
    
    download_image(image_path, 'resources/tmp.jpg')
    image_path = 'resources/tmp.jpg'
    
    # Check if the path exists
    if not os.path.exists(image_path):
        return jsonify({'status': -1, 'message': 'File path does not exist'}), 400
    
    # Check if the file is in jpg or png format
    if not (image_path.endswith('.jpg') or image_path.endswith('.png')):
        return jsonify({'status': -2, 'message': 'File format must be JPG or PNG'}), 400
    
    # Call the health function
    health_result = health(image_path)
    delete_temp_file(image_path)
    
    # Check the result
    if health_result is None:
        return jsonify({'status': -3, 'message': 'Plant ID API call returned None'}), 500
    
    return jsonify({'status': 0, 'result': json.loads(health_result)}), 200

if __name__ == '__main__':
    app.run(debug=True)
