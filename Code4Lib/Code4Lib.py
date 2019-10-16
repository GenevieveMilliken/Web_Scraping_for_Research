# captures the following: 
# article URL, title, author, abstract, issue URL, issue number, and date

from bs4 import BeautifulSoup
import requests
import json
import time

all_my_data = []

url = 'https://journal.code4lib.org/issues'

archives = requests.get(url)
archives_html = archives.text 
soup = BeautifulSoup(archives_html, 'html.parser')

articles = soup.find_all('h3', attrs = {'class': 'articletitle'})

my_data = {
		"article_URL": None,
		"title": None, 
		"author": None,
		"abstract": None,
		"issue_URL": None,
		"issue_number": None, 
		"issue_date": None,
	}

for article in articles: 

	# print('--------------------')

	# get article URL
	article_link = article.find('a')
	article_link_href = article_link['href']
	my_data['article_URL'] = article_link_href

	# get article title
	article_title = article_link.text
	my_data['title'] = article_title 

	# turn each article into a soup item
	article_item = requests.get(article_link_href)
	article_html = article_item.text 
	article_soup = BeautifulSoup(article_html, 'html.parser')

	# get article abstract
	abstract = article_soup.find('div', attrs= {'class': 'abstract'})
	abstract = abstract.text
	my_data['abstract'] = abstract

	# get single and multi-authors with for loop
	authors = article_soup.find_all('meta', attrs={'name': 'citation_author'})

	author_list = []

	for author in authors:
		each_author = author['content']
		author_list.append(each_author)
		my_data['author'] = author_list

	#get issue URL
	issue_link = article_soup.find('p', attrs={'id': 'issueDesignation'})
	issue_link = issue_link.find('a')
	issue_link = issue_link['href']
	my_data['issue_URL'] = issue_link

	# get issue number
	issue_number = article_soup.find('meta', attrs={'name': 'citation_issue'})
	issue_number = issue_number['content']
	my_data['issue_number'] = issue_number

	# get issue date
	issue_date = article_soup.find('meta', attrs={'name': 'citation_publication_date'})
	issue_date = issue_date['content']
	my_data['issue_date'] = issue_date

	time.sleep(1)

	# print(my_data)
	
	all_my_data.append(my_data)	

with open('Code4Lib.json', 'w') as file_object:
	json.dump(all_my_data, file_object, indent=2)
	print("Code4Lib JSON file is Ready")

	
	

	

	



























