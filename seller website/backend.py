from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # Save the user data to the database
        return redirect(url_for('index'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Authenticate user
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/upload', methods=['POST'])
def upload():
    product_name = request.form['product_name']
    price = request.form['price']
    description = request.form['description']
    photos = request.files.getlist('photos')
    video = request.files['video']
    # Save files and details to the database
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
