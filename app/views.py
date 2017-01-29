from flask_cors import CORS
from flask import render_template, request, jsonify
from app import app
import input_categorize

CORS(app)

@app.route('/index', methods=["POST"])
def index():
	data = request.form.to_dict()
	print(data)
	temp = input_categorize.main(data['param'])
	return jsonify(temp)