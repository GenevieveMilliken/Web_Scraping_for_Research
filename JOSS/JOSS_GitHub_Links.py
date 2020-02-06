
from bs4 import BeautifulSoup
import requests
import json
import time

all_my_data = []

for pages in range (0,78):
	url = f"https://joss.theoj.org/papers/published?page={pages*1}"

	results_page = requests.get(url)
	page_html = results_page.text
	soup = BeautifulSoup(page_html, "html.parser")

	articles = soup.find_all('entry')

	my_data = {
		"Article_url": None,
		"Article_title": None,
		"GitHub_URL": None,
		
		}

	for article in articles: 

		time.sleep(5)

		article_links = article.find('link')
		absolute_url = article_links['href']
		my_data["Article_url"] = absolute_url
		# print(absolute_url)

		item_request = requests.get(absolute_url)
		item_html = item_request.text
		item_soup = BeautifulSoup(item_html, "html.parser")
		# print(item_soup)

		article_title = item_soup.find("title")
		article_title = article_title.text
		my_data["Article_title"] = article_title
		# print(article_title)

		GitHub_link = item_soup.find_all("a", attrs={"class": "btn"})
		GitHub_link = GitHub_link[1]['href']
		my_data["GitHub_URL"] = GitHub_link
		# print(GitHub_link)

	# append data dictionary into list
	all_my_data.append(my_data)
# # 	# print(all_my_data)

# write out json
with open('JOSS_GitHub_URLs.json', 'w') as file_object:
	json.dump(all_my_data, file_object, indent=2)
	print("Your file is Ready!")


