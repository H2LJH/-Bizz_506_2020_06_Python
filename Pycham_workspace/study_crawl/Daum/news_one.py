import requests
from bs4 import BeautifulSoup


url = 'https://news.v.daum.net/v/20200615220011696'
req = requests.get(url)

if req.status_code == 200:
    print('ok')

else:
    print('find not')

soup = BeautifulSoup(req.text, 'html.parser')

title = soup.select('h3.tit_view')
content = soup.select('div#harmonyContainer p')
print(title[0].text)
print('==========================================================')
text = ''
for i in content:
    text += i.text

print(text)