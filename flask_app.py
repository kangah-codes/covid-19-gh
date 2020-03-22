from flask import Flask, render_template, url_for, abort
from scraper import get_data
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import datetime

app = Flask(__name__)

@app.route('/')
def index():
	try:
		url = "https://ghanahealthservice.org/covid19/"
		req = Request(url, headers={'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'})
		webpage = urlopen(req).read()
		page_soup = soup(webpage, 'html.parser')
		item = page_soup.findAll('p', {'class':'information-line-text'})
		data = {}
		dat = get_data()
		data['new_cases'] = dat['new_cases']
		data['new_deaths'] = dat['new_deaths']
		data['bool'] = True
		data['new'] = []
		for i in item:
			print(i.text)
			data['new'].append(i.text)
		print(data['new'])
		now = datetime.datetime.now()
		data['now'] = now
		return render_template('index.html', **data)
	except Exception as e:
		data['bool'] = False
		print("errpr")
		data = get_data()
		now = datetime.datetime.now()
		data['now'] = now
		return render_template('index.html', **data)

@app.errorhandler(500)
def handler(error):
	return render_template('error.html')

if __name__ == "__main__":
	app.run(debug=True)