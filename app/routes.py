from flask import render_template, request

from app import app

from .featuring import get_featuring


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/get_featuring', methods=['POST'])
def get_featuring_route():
    data = request.form.to_dict()
    return get_featuring(data['artist_1'], data['artist_2'])
