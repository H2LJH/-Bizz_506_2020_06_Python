import requests
from bs4 import BeautifulSoup


list_url = 'http://news.sarangbang.com/bbs.html?tab=free&p=2'
req = requests.get(list_url)
cnt = 0

if req.status_code != 200:
    print('잘못된 URL')

soup = BeautifulSoup(req.text, 'html.parser')
bord_list = soup.select('tbody#bbsResult > tr > td > a')

for i, href in enumerate(bord_list):
    if i % 2 == 0:
        cnt += 1
        # 제목, 내용, 작성일자, 작성자
        url = 'http://news.sarangbang.com/' + href['href']
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')

        if req.status_code != 200:
            print('잘못된 URL')

        title = soup.select('h3.tit_view')[0].text.strip()
        writer = soup.select('a.name_more')[0].text.strip()
        reg_date = soup.select('span.tit_cat')[1].text.strip()[:10]
        contents = soup.select('div.bbs_view p')

        content = ''
        for j in contents:
            content += j.text.strip()

        print('TITLE    :', title)
        print('Writer   :', writer)
        print('day      :', reg_date)
        print('Contents :\n', content, '\n')

print('사랑방 부동산 에서 {}건의 게시글을 수집 하였습니다.'.format(cnt))