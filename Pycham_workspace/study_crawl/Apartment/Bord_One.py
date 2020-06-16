# 제목
# 내용
# 작성일자
# 작성자

import requests
from bs4 import BeautifulSoup

url = 'http://news.sarangbang.com/talk/bbs/free/163946?url=%2F%2Fnews.sarangbang.com%2Fbbs.html%3Ftab%3Dfree'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

if req.status_code != 200:
    print('잘못된 URL')


title = soup.select('h3.tit_view')[0].text.strip()
writer = soup.select('a.name_more')[0].text.strip()
reg_date = soup.select('span.tit_cat')[1].text.strip()[:10]
contents = soup.select('div.bbs_view p')

content = ''
for i in contents:
    content += i.text.strip()

print('TITLE    :', title)
print('Writer   :', writer)
print('day      :', reg_date)
print('Contents :\n', content)
