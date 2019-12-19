# script currently not working because JOSS changed their web interface 

#import modules
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
	# print(soup)

	articles = soup.find_all('entry')

	for article in articles:
	

		print('----------------')

		time.sleep(5)


# 	for article in articles: 

# 		my_data = {
# 		"Article_url": None,
# 		"Title": None,
# 		"PDF_link": None,
# 		"Date": None,
# 		"Citation": None,
# 		"DOI": None,
# 		"Software_repository_link": None, 
# 		"Paper_review_link": None,
# 		"Software_archive_link": None,

# 		}


		article_links = article.find('link')
		absolute_url = article_links['href']
		# my_data["Article_url"] = absolute_url
		print(absolute_url)

		#stuck here because the html is not encoding properly

		item_request = requests.get(absolute_url)
		item_html = item_request.text
		item_soup = BeautifulSoup(item_html, "html.parser")
		print(item_soup)

# 		title = item_soup.find("meta", attrs={'property': 'og:title'})
# 		# title_only = title['content']
# # 		my_data["Title"] = title_only
# 		print(title)

# 		pdf = item_soup.find("meta", attrs={'name': 'citation_pdf_url'})
# 		pdf_only = pdf['content']
# 		my_data['PDF_link'] = pdf_only
# 		# print(pdf_only)

# 		date = item_soup.find("meta", attrs={'name': 'citation_publication_date'})
# 		date_only = date['content']
# 		my_data['Date'] = date_only
# 		# print(date_only)

# 		citation = item_soup.find("meta", attrs={'property': 'og:description'})
# 		citation_only = citation['content']
# 		my_data['Citation'] = citation_only
# 		# print(citation_only)
		
# 		doi = item_soup.find("meta", attrs={'name': 'citation_doi'})
# 		doi_only = doi['content']
# 		my_data["DOI"] = doi_only
# 		print(doi_only)

# 		software_repo = item_soup.find('div', attrs ={'col-md-3 paper-sidebar'})
# 		software_repo_link = software_repo.find('a')
# 		print(software_repo_link)

# # 	paper_review_link = 

# # 	software_archive_link = 


# # 	#append data dictionary into list
# # 	all_my_data.append(my_data)
# # 	# print(all_my_data)

# # # write out json
# # with open('JOSS_Articles.json', 'w') as file_object:
# # 	json.dump(all_my_data, file_object, indent=2)
# # 	print("Your JOSS JSON file is Ready")


