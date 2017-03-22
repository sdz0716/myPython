#! python3
# find404.py - find out 404 status URL

import requests
import bs4

res = requests.get('https://www.baidu.com')

soup = bs4.BeautifulSoup(res.text, 'html.parser')

i = 0
while i < len(soup.select('a[href]')):
    try:
        html = soup.select('a[href]')[i].get('href')
        resHtml = requests.get(html)
        print(html)
        print(resHtml.status_code)
    except:
        print(html)
        print(400)
    i = i + 1

# print(len(soup.select('a[href]')))