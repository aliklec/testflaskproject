from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random')
def get_random_number():
    number = random.randint(1, 100)
    return jsonify({"number": number})
