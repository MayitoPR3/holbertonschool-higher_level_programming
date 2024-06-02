#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# User Data
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("adminpassword"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    """Basic Authentication"""
    if username in users and check_password_hash(users[username]['password'], password):
        return username


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Protected Route with Basic Authentication"""
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """Token-based Authentication with JWT"""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username in users and check_password_hash(users[username]['password'], password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify({"error": "Invalid username or password"}), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """JWT Protected Route"""
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Role-based Protected Route"""
    current_user = get_jwt_identity()
    if users[current_user]['role'] != 'admin':
        return jsonify({"error": "Forbidden"}), 403
    return "Admin Access: Granted"


if __name__ == '__main__':
    app.run(debug=True)
