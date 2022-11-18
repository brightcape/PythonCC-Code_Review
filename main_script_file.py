import requests
from bs4 import BeautifulSoup
import csv
import os.path

def GenerateHtml(base_url,payload):

	r = requests.get(base_url, params=payload)
	print ("Your'r on" ,r.url)
	html_doc= (r.content)
	return html_doc	

def parsing_and_scrape_data(raw_data):
		
		
		soup = BeautifulSoup(raw_data,'html.parser')
		g_data= (soup.find_all('div',{"class":"g"}))
		
		for items in g_data:
			product_details={}
			atag= items.a
			cite= items.cite
			title = (atag.text)
			link=(cite.text)
			print (link)
			product_details["Title"]=title
			product_details["Links"]=link
			write_on_csv(product_details)
		
		


def write_on_csv(data):

	file_exists = os.path.isfile('googleresults.csv')
	with open ('googleresults.csv', 'a',newline='') as csvfile:
		fieldnames = ['Title', 'Links']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		
		if not file_exists:
			writer.writeheader()
		
		writer.writerow(data)
		print ('wrote on to the file')
