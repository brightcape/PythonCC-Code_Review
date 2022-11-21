import requests
from bs4 import BeautifulSoup
import csv
import os.path


def generate_html(url: str, payload=None) -> bytes:
	"""

	:param base_url:
	:param payload: Data sent in the request
	:return:
	"""
	response = requests.get(url, params=payload)
	print("You're on", response.url)
	html_doc = response.content
	return html_doc


def parse_data(html_doc: bytes) -> BeautifulSoup:
	return BeautifulSoup(html_doc, 'html.parser')


def scrape_data(soup):

		column_data = soup.find_all({'div': 'column'})
		for items in column_data:  # TODO Investigate if we can get rid of the for-loop
			# Loop over all hyperlink sections
			tbd = items.find_all('a')
			for a in tbd:
				link = a.get('href')
				if 'onze-bieren' in link:
					print(link)
					product_details = {
						"Title": a.text,
						"Links": link
					}
					write_on_csv(product_details)  # TODO write csv at once after loading all data
		
		


def write_on_csv(data, file_name='googleresults.csv'):

	file_exists = os.path.isfile(file_name)
	with open (file_name, 'a',newline='') as csvfile:
		fieldnames = ['Title', 'Links']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		
		if not file_exists:
			writer.writeheader()
		
		writer.writerow(data)
		print ('wrote on to the file')


if __name__ == '__main__':
	url = 'https://100watt.nl/brouwerij/onze-bieren/'
	raw_data = generate_html(url)
	parsed_data = parse_data(raw_data)
	scrape_data(parsed_data)