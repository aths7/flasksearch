# Packages
from flask import render_template, jsonify, request

# Methods
from flasksearch import app
from flasksearch.scan_hsn_database import search_text

# Creating Routes
# HTML ROUTES


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

# JSONROUTES


@app.route('/json')
@app.route('/json/home', methods=['GET'])
def json_home():
    return jsonify({"Name": "Atharva"})


@app.route('/json')
@app.route('/json/search', methods=['POST'])
def json_send_email():
    output = search_text(request.json['search_text'])
    return jsonify(output)
