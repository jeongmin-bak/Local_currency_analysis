# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 10:02:30 2021

@author: jungmin
"""
from selenium import webdriver
import time
import sqlite3
import pandas as pd

## 구글스토이 경기지역화폐 크롤링
#def crawling_local_currency():
url = "https://play.google.com/store/apps/details?id=gov.gyeonggi.ggcard&showAllReviews=true"
driver = webdriver.Chrome("./chromedriver.exe")
driver.get(url)

SCROLL_PAUSE_TIME = 10
count = 0
last_height = driver.execute_script("return document.body.scrollHeight")
     # (1) 4번의 스크롤링
for i in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
#    driver.find_element_by_xpath("//*[@id='fcxH9b']/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div[2]/div/span/span").click()
reviews = driver.find_elements_by_xpath("//span[@jsname='bN97Pc']")
dates = driver.find_elements_by_xpath("//span[@class='p2TkOb']")
stars = driver.find_elements_by_xpath("//span[@class='nt2C1d']/div[@class='pf5lIe']/div[@role='img']")

res_dict = []
for i in range(len(reviews)):
    res_dict.append({ 'DATE' : dates[i].text, 'STAR' : stars[i].get_attribute('aria-label'),'REVIEW' : reviews[i].text })

res_df = pd.DataFrame()
res_df = res_df.append(res_dict)
res_df = res_df.rename_axis('idx').reset_index()

print(res_df)
star_list = res_df.STAR.tolist()
starss = []
for i in range(0, len(star_list)):
    starss.append(int(star_list[i][10]))
## 크로링 데이터 데이터베이스에 저장
## 경기지역화폐 평점별 그래프로 표현
import matplotlib.pyplot as plt

ratio = [starss.count(1),starss.count(2),starss.count(3),starss.count(4),starss.count(5)]
labels = ['1점','2점','3점','4점','5점']
plt.rc('font', family = 'Malgun Gothic')
plt.title("경기지역화폐 어플 별점")
plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False)
plt.show()

#return res_df

#def db_insert(tbl):

con = sqlite3.connect("./local_currency.db")
cur = con.cursor()

for row in res_df.itertuples():
    sql = "insert into google_review(idx, date, star, text) values (?,?,?,?)"
    cur.execute(sql, (row[1], row[2], row[3], row[4]))
con.commit()
print("완료")


