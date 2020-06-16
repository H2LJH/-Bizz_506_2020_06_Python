import requests
from bs4 import BeautifulSoup

url = 'https://news.daum.net/breakingnews/digital'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

url_list = soup.select('ul.list_allnews a.link_txt')

for i in url_list:
    url = i['href']
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    title = soup.select('h3.tit_view')
    content = soup.select('div#harmonyContainer p')

    text = ''
    for i in content:
        text += i.text
    print('================================================================================================')
    print(title[0].text)
    print(text)