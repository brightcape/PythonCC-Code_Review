import os.path
import csv


def write_on_csv(data):

	file_exists = os.path.isfile('googleresults.csv')

	with open ('googleresults.csv', 'a',newline='') as csvfile:
		fieldnames = ['Title', 'Links']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		if not file_exists:
			writer.writeheader()
		
		writer.writerow(data)
		print ('wrote on to the file')

data = {'Title': 'Sourcebits mobile app development and design', 'Links': 'sourcebits.com/'}
print (write_on_csv(data))