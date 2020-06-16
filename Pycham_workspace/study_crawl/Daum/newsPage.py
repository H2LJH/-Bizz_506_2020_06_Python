import requests
from bs4 import BeautifulSoup

cnt = 0 # 뉴스기사 개수

for i in range(1, 4):
    url = 'https://news.daum.net/breakingnews/digital?page={}'.format(i)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    url_list = soup.select('ul.list_allnews a.link_txt')

    for j in url_list:
        cnt += 1
        url = j['href']
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        title = soup.select('h3.tit_view')
        content = soup.select('div#harmonyContainer p')

        text = ''
        for k in content:
            text += k.text

        print('================================================================================================\n')
        print(title[0].text, '\n')
        print(text, '\n')


print('===========================')
print('{}건의 뉴스 기사'.format(cnt))
print('===========================')
