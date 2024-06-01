#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
}


@app.route('/')
def home():
    """endpoint, Returns a welcome message"""

    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """endpoint, return usernames"""

    return jsonify(list(users.keys()))


@app.route('/status')
def get_status():
    """endpoint, checks API status"""

    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """endpoint, details by username.
    """

    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """endpoint to add a new user
     Accepts JSON data with user details
     and adds it to the user dictionary.
    """

    data = request.json
    if data:
        username = data.get('username')
        if username:
            users[username] = {
                "name": data.get("name"),
                "age": data.get("age"),
                "city": data.get("city")
            }
            return jsonify({"message": "User added successfully", "user": users[username]}), 201
    return jsonify({"error": "Invalid data provided"}), 400


if __name__ == "__main__":
    app.run(debug=True)
