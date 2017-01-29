from flask import Flask, render_template, request, url_for
from app import app
import subprocess
import input_categorize

@app.route('/generateResponse', methods=['POST'])
def index():
	resp = flask.Response("Foo bar baz")
	resp.headers['Access-Control-Allow-Origin'] = '*'
	return resp
