import requests
from bs4 import BeautifulSoup
import json

html_page = requests.get('https://www.buzzfeed.com/jamiejones/100-food-memes')
soup = BeautifulSoup(html_page.content, 'html.parser')

dict = {"links": []}

for item in soup.find_all('img'):
    dict['links'].append(item['src'])

with open(r'C:\Users\dell\Desktop\Thapar Info\Software Engineerig\PROJECT\JSON Files\links.json', 'w') as fp:
    json.dump(dict, fp, indent=4)
