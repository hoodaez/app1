# Simple E-commerce Platform using Flask

from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Use a secure randomly generated secret key

# Temporary in-memory storage for users and products
users = []
products = []

# Home page displaying all products
@app.route('/')
def home():
    return render_template('home.html', products=products)

# User registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if any(user['username'] == username for user in users):
            flash('Username already exists!')
            return redirect(url_for('register'))
        
        users.append({'username': username, 'password': password})
        flash('Registration successful! Please login.')
        return redirect(url_for('login'))

    return render_template('register.html')

# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = next((user for user in users if user['username'] == username and user['password'] == password), None)
        
        if user:
            flash('Login successful!')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password!')

    return render_template('login.html')

# Add a product
@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        product_name = request.form['product_name']
        price = request.form['price']
        description = request.form['description']
        
        products.append({
            'name': product_name,
            'price': price,
            'description': description
        })

        flash('Product added successfully!')
        return redirect(url_for('home'))

    return render_template('add_product.html')

# Run the application
if __name__ == '__main__':
    # Disable debug mode to avoid multiprocessing issues in some environments
    app.run(debug=False)
