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

    usernames = list(users.keys())
    return jsonify(usernames)


@app.route('/status')
def get_status():
    """endpoint, checks API status"""

    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """endpoint, details by username.
    """

    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"})


@app.route('/add_user', methods=['POST'])
def add_user():
    """endpoint to add a new user
     Accepts JSON data with user details
     and adds it to the user dictionary.
    """

    data = request.get_json()
    if data:
        username = data.get('username')
        if username:
            users[username] = data
            return jsonify({"message": "User added", "user": data})
        else:
            return jsonify({"error": "Username not provided"}), 400
    else:
        return jsonify({"error": "Invalid JSON"}), 400


if __name__ == "__main__":
    app.run(debug=True)
