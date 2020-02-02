from bs4 import BeautifulSoup
import requests
import re
import json

price_finder = re.compile('2[5-8][0-9]|29[0-9]|3[0-9]{2}|400\s€/mēn')

url="https://www.ss.lv/lv/real-estate/flats/riga/agenskalns/hand_over/rss/"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")
#print(soup.prettify()) # print the parsed data of html

for link in soup.find_all('item'):
    price = link.find(text=re.compile("€/mēn"))
    href = link.get("href")
    print(price, href)
    
    




