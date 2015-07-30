from ToppTrack import app
from flask import request, render_template, redirect, url_for

@app.route('/', methods=['GET'])
def index():
	return render_template('home.html')