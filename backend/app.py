from flask import Flask, request, jsonify

from db.login import is_valid_email, is_valid_password, login, signup
from db.get import get_fruits, get_listings, get_user_sales, get_vegetables

app = Flask(__name__)

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
    status = signup(data['email'], data['password'], data['first_name'], data['last_name'])
    return jsonify({'status': status})

@app.route('/api/get_user_sales', methods=['GET'])
def api_get_user_sales():
    email = request.args.get('email')
    status, sales = get_user_sales(email)
    return jsonify({'status': status, 'sales': sales})

# @app.route('/api/get_listings', methods=['GET'])
# def api_get_listings():
#     email = request.args.get('email')
#     status, listings = get_listings(email)
#     return jsonify({'status': status, 'listings': listings})

@app.route('/api/get_vegetables', methods=['GET'])
def api_get_vegetables():
    email = request.args.get('email')
    status, vegetables = get_vegetables(email)
    return jsonify({'status': status, 'vegetables': vegetables})

@app.route('/api/get_fruits', methods=['GET'])
def api_get_fruits():
    email = request.args.get('email')
    status, fruits = get_fruits(email)
    return jsonify({'status': status, 'fruits': fruits})

if __name__ == '__main__':
    app.run(debug=True)
