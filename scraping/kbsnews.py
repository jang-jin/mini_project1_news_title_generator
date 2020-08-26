import requests
from bs4 import BeautifulSoup
import csv
import json
import pandas as pd

dt_list = pd.date_range(start='20200101', end='20200826').strftime("%Y%m%d").tolist()

for dt in dt_list:
    cookies = {
        '_ga': 'GA1.3.1442193288.1596155169',
        'STAT_WEBLOG_TOKEN': '715275f3-edbe-416f-bfa5-86d1d6eeb5a0',
        '_gid': 'GA1.3.112270997.1598420836',
        'STAT_WEBLOG_SESSION_ID': '8d7a963c-fd77-4739-9264-efd4ec28ba5e',
        'JSESSIONID': '91E69BF8E3AD9D1E3C95491AB86B3D36',
    }

    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://news.kbs.co.kr',
        'Referer': 'http://news.kbs.co.kr/news/list.do?ctcd=0007&ref=pMenu',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    data = {
    'CURRENT_PAGE_NO': '1',
    'ROW_PER_PAGE': '12',
    'SEARCH_DATE': dt,
    'SEARCH_CONTENTS_CODE': '0007',
    'LAST_DATE': '20200826'
    }

    response = requests.post('http://news.kbs.co.kr/news/getContentsNewsList.do', headers=headers, cookies=cookies, data=data, verify=False)

    json_data = json.loads(response.text)

    try:
        for page in json_data['page_list']:
            URL = f"http://news.kbs.co.kr/news/view.do?ncd={page['NEWS_CODE']}"
            response = requests.get(URL)
            soup = BeautifulSoup(response.text, "html.parser")

            news_data = {
                            "date":dt,
                            "title":soup.select_one('.tit-s').text,
                            "content":soup.select_one('#cont_newstext').text.strip().replace('  ', ' ')
                        }
            with open("./scraping/kbsnews.csv", "a", encoding="utf-8", newline="") as csvfile:
                fieldnames = ["date", "title", "content"]
                csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
                csvwriter.writerow(news_data)
    except:
        continue
