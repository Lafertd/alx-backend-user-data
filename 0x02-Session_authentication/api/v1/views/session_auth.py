from flask import request, jsonify, make_response
from api.v1.app import auth
from models.user import User

# Route to handle user login with session authentication
@app.route('/api/v1/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    # Retrieve email and password from the form data
    email = request.form.get('email')
    password = request.form.get('password')

    # Check if email is missing or empty
    if not email:
        return jsonify({"error": "email missing"}), 400
    
    # Check if password is missing or empty
    if not password:
        return jsonify({"error": "password missing"}), 400
    
    # Retrieve user based on email
    user = User.search(email)
    
    # If no user found, return error
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    
    # Check if password is valid
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    
    # Create a session for the user
    session_id = auth.create_session(user.id)
    
    # Create response with user's JSON representation
    user_json = user.to_json()
    
    # Set the session ID in a cookie
    response = make_response(jsonify(user_json))
    response.set_cookie(auth.SESSION_NAME, session_id)
    
    return response

