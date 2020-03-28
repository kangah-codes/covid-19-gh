import requests
import lxml.html as lh
import pandas as pd
import covid19cases as covid


def get_data():
	url = "https://www.worldometers.info/coronavirus"

	page = requests.get(url)

	doc = lh.fromstring(page.content)

	tr_elements = doc.xpath('//tr')

	col = []
	i = 0

	for t in tr_elements[0]:
		 i += 1
		 name = t.text_content()
		 col.append((name, []))

	for j in range(1, len(tr_elements)):
		T = tr_elements[j]

		if len(T) != 10:
			break

		i = 0

		for t in T.iterchildren():
			data = t.text_content()
			if i > 0:
				try:
					data = int(data)
				except:
					pass
			col[i][1].append(data)
			print(col)
			i += 1

	Dict = {title: column for (title, column) in col}

	df = pd.DataFrame(Dict)


	search = df[df["Country,Other"].astype(str).str.match("Ghana")].head(1)

	return {
		"total_cases": (search["TotalCases"]),
		"total_deaths": (search["TotalDeaths"]),
		"total_recovered": (search["TotalRecovered"]),
		"active_cases": (search["ActiveCases"]),
		"new_cases": search["NewCases"],
		"new_deaths": search["NewDeaths"].values
	}

	#return {}

print(get_data())