from urllib.request import urlopen#用于获取网页
from bs4 import BeautifulSoup#用于解析网页

html = urlopen('https://www.douban.com/')
bsObj = BeautifulSoup(html, 'html.parser')
t1 = bsObj.find_all('a')
for t2 in t1:
    t3 = t2.get('href')
    print(t3)

t2 = bsObj.find_all('img')
for t in t2:
    t4 = t.get('src')
    print(t4)