# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 21:41:38 2021

@author: Adminb
"""
# KNI: KONA I
# 코나아이의 종가와 거래량
# csv 파일은 data.krx.co.kr 에서 다운로드
# 2019년 1월 2일 - 2021년 4월 12일 기준

import csv
import matplotlib.pyplot as plt

f = open('./KNI.csv')
data = csv.reader(f)
next(data)

close = []
mc = []
date = []
amount = []
max_close = []
max_date = []

for row in data:
    date.append(row[0])
    mc.append(int(row[9]))
    close.append(int(row[1]))
    amount.append(int(row[7]))
    if row[0] == '2019/06/21':
        max_date.append(row[0])
        max_close.append(int(row[1]))
    if row[0] == '2020/10/22':
        max_date.append(row[0])
        max_close.append(int(row[1]))
    if row[0] == '2021/02/22':
        max_date.append(row[0])
        max_close.append(int(row[1]))
        

close.reverse()
mc.reverse()
amount.reverse()
date.reverse()
max_close.reverse()
max_date.reverse()

# print(close)
# print(mc)
# print(date)

plt.figure(figsize = (20, 5), dpi = 300)
plt.title('KONA I Closing Value')
plt.plot(date, close, 'green', label = 'Close')
plt.plot(max_date, max_close, 'r^', label = 'Peak')
plt.xticks(max_date, rotation = 15)
# plt.locator_params(axis='x', nbins=len(date)/130)
plt.legend(loc = 'best')
plt.grid(True)


plt.figure(figsize = (30, 5), dpi = 300)
plt.title('KONA I Trading Volume')
plt.bar(date, amount, label = 'Trading')
plt.xticks(date)
plt.locator_params(axis='x', nbins=len(date)/130)
plt.legend(loc = 2)
plt.show()

    
