import sqlite3
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from konlpy.tag import Kkma

## 형태소 분석

dbname='./local_currency.db'
def getData(cols='*', whr='', tblname='google_review'):
    with sqlite3.connect(dbname) as conn:
        cur = conn.cursor()
        sql = 'select ' + cols + ' from ' + tblname + ' ' + whr
        data = cur.execute(sql).fetchall()

    return data

def tknWord(txt):
    kkma = Kkma()
    kpos = kkma.pos(txt)
    cate = ['NNG','MAG','VV','NNP','NNB','VA','VCP','MAG','MAC']
    tkn = []
    for k in kpos:
        if(k[1] in cate):
            if(len(k[0]) > 1):
                tkn.append(k[0])
    return tkn

res = getData('text')
df = pd.DataFrame(res)
review = np.ravel(df)

txta = []
for res in review:
    txta.append(tknWord(res))

txtall=''
for txt in txta:
    txtall +=' '.join(txt)
    txtall +=' '
#txtn = np.ravel(txta)


from wordcloud import WordCloud
from matplotlib import font_manager,rc
import matplotlib.pyplot as plt
font_path="C:\Windows\Fonts\malgun.ttf"
font=font_manager.FontProperties(fname=font_path).get_name()

WC=WordCloud(font_path=font_path,background_color='white',height=1000,width=1000,max_words=100).generate(txtall)
fig=plt.figure(figsize=(5, 5))
plt.imshow(WC)
plt.axis('off')
plt.show()
