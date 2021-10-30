# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import time
import csv
import re

if __name__ == '__main__':
    target = 'https://www.storytel.com/fi/fi/categories/7-Fantasia-scifi'
    req = requests.get(url=target)
    html = req.text
    div_bf = BeautifulSoup(html, 'html.parser')
    div = div_bf.find_all('div', class_ = 'gridBookTitle')
    soup = BeautifulSoup(str(div), 'html.parser')
    title = []
    for bookname in soup.find_all('a'):
        title.append(bookname.string)

    with open('Fantasiascifi.csv','w', newline='', encoding='UTF-8') as file:
            writer = csv.writer(file)
            writer.writerows([title])
