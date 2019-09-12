# this script scrapes metadata for ArXiv articles that contain the word 'github'
# if running this script please consult arXiv's robots.txt file
# must add user-agent information before running

from bs4 import BeautifulSoup
import requests
import json

all_my_data = []

for pages in range (0,5):
	url = f"https://arxiv.org/search/?query=github&searchtype=all&abstracts=show&order=-announced_date_first&size=200"

	headers = {
    'User-Agent': 'Chrome/74.0',
    'From': 'my email address' 
}

	results_page = requests.get(url, headers=headers)
	page_html = results_page.text
	soup = BeautifulSoup(page_html, "html.parser")

	articles = soup.find_all('li', attrs={'class': 'arxiv-result'})

	for article in articles:

		my_data = {
			"Article_Url": None,
			"DOI": None,
			"Article_Title": None,
			"Article_Abstract":None,
			"Article_Subject":None,
			"Article_Date": None,
			"Article_PDF":None,
		}

		print('-------------------')

		article_link = article.find('a')
		abs_url = article_link['href']
		# print(abs_url)
		my_data['Article_Url'] = abs_url

		item_request = requests.get(abs_url, verify=False)
		item_html = item_request.text
		item_soup = BeautifulSoup(item_html, 'html.parser')

		DOIs = item_soup.find_all('td', attrs={'class': 'tablecell arxividv'})
		DOIs = DOIs[0].find('a')
		DOIs = DOIs.text
		# print(DOIs)
		my_data['DOI'] = DOIs

		article_abstract = item_soup.find_all('meta', attrs={'property': 'og:description'})
		article_abstract = article_abstract[0]['content']
		article_abstract = article_abstract.replace("\n", "")
		# print(article_abstract)
		my_data["Article_Abstract"] = article_abstract

		article_subject = item_soup.find_all('td', attrs={'class': 'tablecell subjects'})
		article_subject = article_subject[0].text
		article_subject = article_subject.replace("\n", "")
		# print(article_subject)
		my_data['Article_Subject'] = article_subject

		article_title = item_soup.find_all('meta', attrs={'name': 'citation_title'})
		article_title = article_title[0]['content']
		# print(article_title)
		my_data['Article_Title'] = article_title

		article_pdf = item_soup.find_all('meta', attrs={'name': 'citation_pdf_url'})
		article_pdf = article_pdf[0]['content']
		# print(article_pdf)
		my_data['Article_PDF'] = article_pdf

		article_date = item_soup.find_all('meta', attrs={'name': 'citation_date'})
		article_date = article_date[0]['content']
		# print(article_date)
		my_data['Article_Date'] = article_date

		all_my_data.append(my_data)

# write out json
with open('ArXiv_Articles.json', 'w') as file_object:
	json.dump(all_my_data, file_object, indent=2)
	print("Your JSON file is Ready")


	














		




