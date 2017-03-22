#! python3
# downloadkukudm.py - download jintianyi from kukudm comic

import bs4
import requests
import os
import re
import threading
import time

def partOne(part):
    urlRegex = re.compile(r'(\"\+m20.*\")(.*\.jpg).*style')
    url = 'http://comic.kukudm.com'
    urlSub = '/comiclist/858/%s/1.htm' % part
    os.makedirs('C:\\Users\\daize\\Desktop\\kukudm\\雪灵\\partOne', exist_ok=True)
    i = 1

    # for i in range(4):
    while not urlSub.endswith('exit.htm'):
        urlNow = url + urlSub
        print('Downloading page %s' % urlNow)
        res = requests.get(urlNow)
        res.raise_for_status()

        # jpg download url
        soup = bs4.BeautifulSoup(res.text.encode('latin1').decode('gbk'), "html.parser")
        comicElem = soup.select('script')
        mo = urlRegex.search(str(comicElem[3]))
        mo1 = mo.group(1)
        moHead = re.sub(r'\"\+m201001d\+\"|\"\+m200911d\+\"|\"\+m201304d\+\"', 'http://n.1whour.com/', mo1)     #正则的替换
        # print(mo1)
        urldown = moHead + mo.group(2)
        # print(urldown)
        urlSub = soup.select('a[href]')[-1].get('href')
        # print(urlSub)

        # download and save jpg
        file = open('C:\\Users\\daize\\Desktop\\kukudm\\雪灵\\partOne\\%s.jpg' % i, 'wb')
        file.write(requests.get(urldown).content)       #content可取二进制数据
        file.close()

        i = i + 1
        # exit()
    # return 'partone finish'


def partTwo(part):
    urlRegex = re.compile(r'(\"\+m20.*\")(.*\.jpg).*style')
    url = 'http://comic.kukudm.com'
    urlSub = '/comiclist/858/%s/1.htm' % part
    os.makedirs('C:\\Users\\daize\\Desktop\\kukudm\\雪灵\\partTwo', exist_ok=True)
    i = 1

    # for i in range(4):
    while not urlSub.endswith('exit.htm'):
        urlNow = url + urlSub
        print('Downloading page %s' % urlNow)
        res = requests.get(urlNow)
        res.raise_for_status()

        # jpg download url
        soup = bs4.BeautifulSoup(res.text.encode('latin1').decode('gbk'), "html.parser")
        comicElem = soup.select('script')
        mo = urlRegex.search(str(comicElem[3]))
        mo1 = mo.group(1)
        moHead = re.sub(r'\"\+m201001d\+\"|\"\+m200911d\+\"|\"\+m201304d\+\"', 'http://n.1whour.com/', mo1)  # 正则的替换
        # print(mo1)
        urldown = moHead + mo.group(2)
        # print(urldown)
        urlSub = soup.select('a[href]')[-1].get('href')
        # print(urlSub)

        # download and save jpg
        file = open('C:\\Users\\daize\\Desktop\\kukudm\\雪灵\\partTwo\\%s.jpg' % i, 'wb')
        file.write(requests.get(urldown).content)  # content可取二进制数据
        file.close()

        i = i + 1
        # exit()
    # return 'part two finish'

threadPartOne = threading.Thread(target=partOne, args=[15822])
threadPartTwo = threading.Thread(target=partTwo, args=[15823])
threadPartOne.start()
time.sleep(10)
threadPartTwo.start()

threadList = [threadPartOne, threadPartTwo]     #需使用变量，不能用字符串
for i in threadList:
    threadPartOne.join()
    print('%s done' % i)
    #输出
    # <Thread(Thread-1, stopped 23376)> done
    # <Thread(Thread-2, started 91900)> done
print('cody finish')

