#! python3
# lucky.py - opens several baidu search results

import sys
import requests
import webbrowser
import bs4

print('baiduing...')
res = requests.get('http://www.baidu.com/s?wd=' + ' '.join(sys.argv[1:]))

soup = bs4.BeautifulSoup(res.text)

linkElems = soup.select('.t a')

num = min(5, len(linkElems))
for i in range(num):
    webbrowser.open(linkElems[i].get('href'))