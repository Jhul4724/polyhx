from flask import Flask, request, jsonify
from typing import Any, Tuple

from db.edit_listings import remove_listing, sell_from_listing
from db.login import is_valid_email, is_valid_password, login, signup
from db.get import get_fruits, get_listings, get_user_sales, get_vegetables
from db.post import create_new_sale

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
