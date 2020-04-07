from flask import Flask, render_template, url_for, abort
from scraper import get_data
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import datetime
import covid19cases as covid

# import HTMLSession from requests_html
# create an HTML Session object

app = Flask(__name__)

places = [
	[5.6037, -0.1870],
	[5.6879, -0.0373],
	[5.6683, -0.0379],
	[5.6995, -0.0583],
	[5.56, -0.4],
	[5.5833, -0.1000],
	[5.7142, -0.1542],
	[ 5.6931, -0.0327],
	[ 5.6784, -0.1713],
	[ 5.5752, -0.1468],
	[ 5.587938, -0.238539],
	[ 5.5820, -0.2557],
	[ 5.5512, -0.2526],
	[ 5.5112, -0.2848],
	[ 5.6142, -0.1963],
	[ 5.6553, -0.2784],
	[ 5.6667, -0.3560],
	[ 5.5666, -0.3335],
	[ 5.5774, -0.3137],
	[ 5.5195, -0.4880],
	[ 6.7252, -1.6566],
	[ 6.7226, -1.6445],
	[ 6.2335, -0.3972],
	[ 5.8118, -1.8974],
	[ 6.7175, -1.5620],
	[ 6.6905, -1.6494],
	[ 6.5972, -1.5790],
	[ 6.8540, -1.5790],
	[ 6.7151, -1.5091],
	[6.540490, -1.476450],
]

@app.route('/')
def index():
	data = covid.get_country_cases("Ghana")
	data['bool'] = False
	now = datetime.datetime.now()
	data['now'] = now
	data['places'] = places
	return render_template('index.html', **data)

@app.errorhandler(500)
def handler(error):
	return render_template('error.html')

	

if __name__ == "__main__":
	app.run(debug=True)