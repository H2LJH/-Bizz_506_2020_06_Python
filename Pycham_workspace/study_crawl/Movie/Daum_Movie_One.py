import requests
from bs4 import BeautifulSoup

# 작성자, 평점, 내용, 작성일자
cnt = 0
page = 1
while True:
    url = 'https://movie.daum.net/moviedb/grade?movieId=129134&type=netizen&page={}'.format(page)
    req = requests.get(url)

    if req.status_code != 200:
        print("URL Error")

    soup = BeautifulSoup(req.text, 'html.parser')
    reply_list = soup.select('div.review_info')

    if len(reply_list) == 0:
        print('마지막 페이지 입니다.')
        break;

    print('page : {}'.format(page), '■■■■■■■■■■■■■■■■■■■■■■■■■■\n')
    for reply in reply_list:
        cnt += 1
        writer = reply.select('em.link_profile')[0].text.strip()
        score = reply.select('em.emph_grade')[0].text.strip()
        content = reply.select('p.desc_review')[0].text.strip()
        reg_data = reply.select('span.info_append')[0].text.strip()

        print('작성자 :', writer)
        print('평점  : ', score)
        print('내용  :', content)
        index_val = reg_data.index(',')
        print("날짜 :", reg_data[:index_val], '\n')
        print('====================================================\n')
    page += 1
print('댓글 개수 :', cnt)