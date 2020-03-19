from flask import Flask, render_template, url_for
from scraper import get_data
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

app = Flask(__name__)

@app.route('/')
def index():
	url = "https://ghanahealthservice.org/covid19/"
	req = Request(url, headers={'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'})
	webpage = urlopen(req).read()
	page_soup = soup(webpage, 'html.parser')
	item = page_soup.find('span', {'align':'center'})
	data = get_data()
	data['new'] = item.text
	return render_template('index.html', **data)

if __name__ == "__main__":
	app.run(debug=True)