import json

from flask import Flask, render_template

app = Flask(__name__)


# Route for home page
@app.route('/')
def home():
    return render_template('index.html')


# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')


# Route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json', 'r') as f:
        items_data = json.load(f)
    items_list = items_data.get('items', [])  # Retrieve the 'items' list from the loaded JSON data
    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
