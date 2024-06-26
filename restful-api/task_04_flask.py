#!/usr/bin/python3
"""
Module for the API Task
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}


@app.route('/')
def home():
    """endpoint, Returns a welcome message"""
    return "Welcome to the Flask API!"


@app.route('/data', methods=['GET'])
def get_data():
    """endpoint, return usernames"""
    return jsonify(list(users.keys()))


@app.route('/status', methods=['GET'])
def get_status():
    """endpoint, checks API status"""
    return "OK"


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """endpoint, details by username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """endpoint to add a new user"""
    data = request.get_json()
    if data:
        username = data.get('username')
        if not username:
            return jsonify({"error": "Username not provided"}), 400
        elif username in users:
            return jsonify({"error": "Username already exists"}), 400
        else:
            users[username] = data
            return jsonify({"message": "User added", "user": data}), 201
    else:
        return jsonify({"error": "Invalid JSON"}), 400


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
