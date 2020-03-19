from urllib.request import Request, urlopen
url = 'https://ghanahealthservice.org/covid19/'

# now, with the below headers, we defined ourselves as a simpleton who is
# still using internet explorer.
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
req = Request(url, headers = headers)
resp = urlopen(req)
respData = resp.read()

print(respData)