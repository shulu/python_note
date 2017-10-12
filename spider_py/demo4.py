# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

response = requests.get("http://jecvay.com")
soup = BeautifulSoup(response.text, "html.parser")

# print(soup.title.text)
# print(soup.body.text)
for x in soup.findAll("a"):
    print(x['href'])