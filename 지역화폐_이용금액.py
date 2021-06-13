# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 12:10:41 2021

@author: jungmin
"""
import csv
import operator
import matplotlib.pyplot as plt

f = open('./LM.csv', encoding = 'cp949')
data = csv.reader(f)
days = []
header = next(data)
count = 0
city = set()
#19년 4월부터 21년 2월까지 날짜 저장
for row in data:
    if row[0] != '':
        city.add(row[0])
city = list(city)
print(city)
f.seek(0)
header = next(data)
for row in data:
    days.append(row[1])
    count += 1
    if count == 23:
        break
days = list(reversed(days))  
#파일의 맨 처음으로 이동
f.seek(0)
i = 0
city_month_account = []

for x in range(len(city)):
    city_month_account.append([])

for one in city:
    #city_month_account[i].append(one)
    for row in data:
        if one == row[0] and row[4] != '' :
            city_month_account[i].append(int(row[4]))
        if one == row[0] and row[4] == '' and row[6] != '' :
            city_month_account[i].append(int(row[6]))
        if len(city_month_account[i]) == 23:
            break
        
            
    i = i+1
    f.seek(0)
    
for i in range(len(city_month_account)):
    city_month_account[i] = list(reversed(city_month_account[i]))
    
print(city_month_account[0])
print(len(city_month_account[0]))
f.close()
count = 0

plt.figure(dpi = 300)
plt.rc('font', family = 'Malgun Gothic')
plt.subplot(2,2,1)
for i in range(0,7):
    plt.plot(days, city_month_account[i])
plt.legend([city[0],city[1],city[2], city[3], city[4], city[5], city[6]])
plt.xticks([])
plt.subplot(2,2,2)
for i in range(7,13):
     plt.plot(days, city_month_account[i])
plt.legend([city[7],city[8],city[9], city[10], city[11], city[12]])
plt.xticks([])     
plt.subplot(2,2,3)
for i in range(13,19):
     plt.plot(days, city_month_account[i])
plt.legend([city[13],city[14],city[15], city[16], city[17], city[18]])
plt.xticks([]) 
plt.subplot(2,2,4)
for i in range(19,24):
     plt.plot(days, city_month_account[i])
plt.legend([city[19],city[20],city[21], city[22], city[23]])
plt.xticks([])
plt.show()

