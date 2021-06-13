# 코나아이 분기별 매출

import csv
import matplotlib.pyplot as plt

revenue= {}

for x in range(2019, 2021):
    revenue[int('%s'%x)] = []
    for y in range(1, 5):
        f = open('%s_%s.csv'%(x, y)) # csv 파일은 DART의 분기별 보고서 내 손익계산서에서 가져옴
        data = csv.reader(f)
        
        if y == 4:
            for row in data:
                if '매출액' in row[0]:
                    revenue[x].append(int(row[1].replace(',', '')) - sum(revenue[x]))
                    
        for row in data:
            if '매출액' in row[0]:
                revenue[x].append(int(row[1].replace(',', '')))

time = []
for x in range(19, 21):
    for y in range(1, 5):
        time.append("%d' %dQ" % (x, y))
result = revenue[2019] + revenue[2020]

# print(revenue)
# for i in result:
    # print(i)

plt.figure(figsize = (15, 5), dpi = 300)
plt.rc('font', family = 'Malgun Gothic')
plt.title('KONA I 분기별 매출')
plt.bar(time, result)
plt.xticks(time)
plt.show()
