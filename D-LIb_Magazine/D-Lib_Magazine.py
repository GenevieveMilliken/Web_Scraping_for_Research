from bs4 import BeautifulSoup
import requests
import json

all_my_data = []

url = "http://www.dlib.org/title-index.html"

title_index = requests.get(url)
title_index_html = title_index.text 
soup = BeautifulSoup(title_index_html, "html.parser")

articles = soup.find_all("p", attrs = {"class": "archive"})

for article in articles: 

	my_data = {
		"article_URL": None,
		"article_title": None,   
		"article_text":None, 
	}

	# print("---------------")

	article_link = article.find('a')
	url_slug = article_link['href']
	abs_url = "http://www.dlib.org/" + url_slug
	my_data['article_URL'] = abs_url

	item_request = requests.get(abs_url)
	item_html = item_request.text
	item_soup = BeautifulSoup(item_html, "html.parser")

	title = item_soup.find_all('title')
	title_text = title[0]
	title_text = title_text.text
	title_text = title_text.replace("\n", "")
	title_text = title_text.replace("\r", "")
	my_data['article_title'] = title_text
	

	text = item_soup.text
	text = text.replace("\n", "")
	text = text.replace("\r", "")
	my_data['article_text'] = text

	# print(my_data)

	all_my_data.append(my_data)

with open('D-Lib_Magazine.json', 'w') as file_object:
	json.dump(all_my_data, file_object, indent=2)
	print("The JSON file is Ready")








		



















	
