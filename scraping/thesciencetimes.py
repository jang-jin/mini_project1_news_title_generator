import requests
from bs4 import BeautifulSoup
import csv
import json
import pandas as pd

category_list = ['science', 'medicine', 'space', 'nature', 'new-tech', 'ict', 'covid-19']
page_num = 500
for category in category_list:
    for page in range(1, page_num + 1):
        URL = f"https://www.sciencetimes.co.kr/category/sci-tech/{category}/page/{str(page)}/"

        response = requests.get(URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        for a in soup.select('.cate + a'):
            response_news = requests.get(a['href'])
            soup_news = BeautifulSoup(response_news.text, 'html.parser')

            soup_news.select_one('.view_tit_wrap .date span').extract()
            date = soup_news.select_one('.view_tit_wrap .date').text.strip().split(' ')[0].replace('.','')
            soup_news.select_one('.view_tit_wrap .tit p').extract()
            title = soup_news.select_one('.view_tit_wrap .tit').text.strip()
            
            soup_news.select_one('.view_content .resize .bawpvc-ajax-counter').extract()
            content = ""
            for p in soup_news.select('.view_content .resize > p'):
                content += p.text.strip()+ " "
            
            news_data = {
                            "date":date,
                            "title":title,
                            "content":content.strip()
                        }
            with open("./scraping/thesciencetimes.csv", "a", encoding="utf-8", newline="") as csvfile:
                fieldnames = ["date", "title", "content"]
                csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
                csvwriter.writerow(news_data)
    