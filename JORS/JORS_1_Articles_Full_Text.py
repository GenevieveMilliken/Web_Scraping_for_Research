# This script scrapes all published articles from The Journal of Open Research Software
# What is written to JSON includes article URL, DOI, keywords, abstract, and article text

# import modules
from bs4 import BeautifulSoup
import requests
import json
import time

# create empty list for data
all_my_data = []

# use f-string synatax to paginate
for pages in range (0,1):
	url = f"https://openresearchsoftware.metajnl.com/articles/?app=25&%20order=date_published&%20f=1&%20f=2&%20f=3&page={pages*1}"

	#request urls using the requests module 
	#turn webpage into a soup object
	results_page = requests.get(url)
	page_html = results_page.text
	soup = BeautifulSoup(page_html, "html.parser")

	#identify html list for article entries
	articles = soup.find_all('li', attrs= {'class': 'article-block'})

	#loop through list for each article  
	for article in articles:

		#create data dictionary for all fields needed
		my_data ={
			"Article_Title": None,
			"Article_URL": None,
			"DOI": None,
			"Key_Words": None,
			"Article_Abstract": None,
			"Article_Text": None,
		}

		# print('-----------')

		time.sleep(5)

		# get absolute url for each article
		article_link = article.find('a')
		abs_url = "https://openresearchsoftware.metajnl.com" + article_link['href']
		# my_data["Article_URL"] = abs_url

		# turn absolute urls into soup objects
		item_request = requests.get(abs_url)
		item_html = item_request.text
		item_soup = BeautifulSoup(item_html, "html.parser")
		item_soup_text = item_soup.text

		#get title

		Title = item_soup.find("title").text
		my_data["Article_Title"] = Title

		# locate DOI
		DOIs = item_soup.find_all('meta', attrs={'name': 'DC.Identifier.DOI'})
		DOI = (DOIs[0]["content"])
		my_data["DOI"] = DOI
		
# 		# locate keywords metadata field
		key_words = item_soup.find_all('meta', attrs={'name': 'citation_keywords'})
		try:
			keys = key_words[0]["content"]
		except IndexError:
			pass
		my_data["Key_Words"] = keys

		# locate abstract div
		abstract = item_soup.find_all('div', attrs={'class': 'authors'})
		abstract_text = abstract[1]
		abstract_text = abstract_text.text.strip()
		abstract_text = abstract_text.replace("\n"," ")
		my_data["Article_Abstract"] = abstract_text
		
		
		# locate text div
		article_text = item_soup.find_all('div', attrs={'class': 'article-body'})
		try:
			text = article_text[1]
			text = text.text.strip()
			text = text.replace("\n"," ")
			my_data["Article_Text"] = text
		except IndexError:
			text = article_text[0]
			text = text.text.strip()
			text = text.replace("\n"," ")
			text = text.replace("\t","")
			my_data["Article_Text"] = text
# 		
	 	#append data dictionary into a list
		all_my_data.append(my_data)


with open('JORS_Articles.json', 'w') as file_object:
	json.dump(all_my_data, file_object, indent=2)
	print("Your JSON file is Ready")


