# beautifulsoup4 import


import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=081&aid=0003099012'
resp = requests.get(url)

if resp.status_code == 200:
    resp.headers
    
else:
    print('잘못된 URL입니다. 다시 입력해주세요')

soup = BeautifulSoup(resp.text, 'html.parser')
title = soup.find('h3', id='articleTitle')
body = soup.find('div', id='articleBodyContents')

print(title.text)
print('=====================')
print(body.text.strip()) # strip 좌우 여백없애는 함수

# /robots.txt <- 사이트별 크롤링 허용범위