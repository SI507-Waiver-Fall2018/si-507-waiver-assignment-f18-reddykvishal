# these should be the only imports you need

import requests
from bs4 import BeautifulSoup

# write your code here
# usage should be python3 part3.py

url = "https://www.michigandaily.com/"
soup = BeautifulSoup(requests.get(url).content, 'html.parser')

mostRead = soup.find("div", attrs={'class': 'view-most-read'}).find("ol").find_all("li")

print("Michigan Daily -- MOST READ")

for listItem in mostRead:
	print(listItem.find("a").text.strip())

	try:
		innerSoup = BeautifulSoup(requests.get(url + listItem.find("a")['href']).content, 'html.parser')
		author= innerSoup.find("div", attrs = {"class":"byline"}).find('div').find('a').text.strip()
		print("by " + author)

	except:
		print("No byline author found")
