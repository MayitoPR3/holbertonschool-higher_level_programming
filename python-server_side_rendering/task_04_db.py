import csv
import json
from flask import Flask, render_template, request
import sqlite3

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


# Function to read JSON file
def read_json_file():
    with open('products.json', 'r') as json_file:
        data = json.load(json_file)
    return data


# Function to read CSV file
def read_csv_file():
    data = []
    with open('products.csv', 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append(row)
    return data


# Route to display products from different sources
@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error='Wrong source')

    data = []

    if source == 'json':
        data = read_json_file()  # Implement your read_json_file function here
    elif source == 'csv':
        data = read_csv_file()   # Implement your read_csv_file function here
    elif source == 'sql':
        data = fetch_data_from_sqlite()

    # Handle error if data fetching from SQLite fails
    if source == 'sql' and data is None:
        return render_template('product_display.html', error='Database error')

    # Filter by product_id if provided
    if product_id:
        filtered_data = [product for product in data if str(product[0]) == product_id]
        if not filtered_data:
            return render_template('product_display.html', error='Product not found')
        data = filtered_data

    return render_template('product_display.html', products=data)


# Function to fetch data from SQLite database
def fetch_data_from_sqlite():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()

        # Fetch all products from SQLite Products table
        cursor.execute('SELECT id, name, category, price FROM Products')
        products = cursor.fetchall()

        conn.close()

        return products

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return None


if __name__ == '__main__':
    app.run(debug=True, port=5000)
