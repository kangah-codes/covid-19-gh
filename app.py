from flask import Flask, render_template, url_for
from scraper import get_data

app = Flask(__name__)

@app.route('/')
def index():
	data = get_data()
	return render_template('index.html', **data)

app.run(debug=True)