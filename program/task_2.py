# -*- coding: utf-8 -*-

import pylab as pl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
import seaborn as sns
from pandas.core.frame import DataFrame
import matplotlib.font_manager as font_manager
font = font_manager.FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf")
font.set_size(16)

# 读取附件中的数据
data = pd.read_csv("附件1.csv",sep = ',' ,encoding = 'gbk')
A = pd.read_csv("task1-1A.csv",sep = ',' ,encoding = 'utf-8')
B = pd.read_csv("task1-1B.csv",sep = ',' ,encoding = 'utf-8')
C = pd.read_csv("task1-1C.csv",sep = ',' ,encoding = 'utf-8')
D = pd.read_csv("task1-1D.csv",sep = ',' ,encoding = 'utf-8')
E = pd.read_csv("task1-1E.csv",sep = ',' ,encoding = 'utf-8')

def selectMonth6(AA):
    AA['交易时间'] = AA['支付时间']
    AA['支付时间'] = pd.to_datetime(AA['支付时间'])  
    AA = AA.set_index('支付时间') 
    acopy = AA['2017-6-1':'2017-6-30']
    return acopy


data6 = selectMonth6(data)
good6 = data6['商品'].value_counts()

# 6月销量前五柱状图
rects = plt.bar(range(len(good6[0:5])),good6[0:5],tick_label=good6.index[0:5])
plt.title("6月销量前五柱状图",fontproperties=font)
plt.xlabel("商品",fontproperties=font)  
plt.ylabel("销量",fontproperties=font)
plt.xticks(fontproperties=font)  # x轴显示中文
# 添加数据标签
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, height, ha='center', va='bottom')
        
add_labels(rects)

turnover = pd.read_csv("turnover.csv",sep = ',' ,encoding = 'utf-8')


# 各售货机每月交易额折线图
plt.plot(turnover['月份(交易额)'],turnover['A'])
plt.plot(turnover['月份(交易额)'],turnover['B'])
plt.plot(turnover['月份(交易额)'],turnover['C'])
plt.plot(turnover['月份(交易额)'],turnover['D'])
plt.plot(turnover['月份(交易额)'],turnover['E'])
plt.legend()
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])  # 改变x轴刻度
plt.title("各售货机每月交易额",fontproperties=font)
plt.xlabel("月份",fontproperties=font)  
plt.ylabel("交易额（元）",fontproperties=font)

#  第二种：每月各售货机交易额折线图
turnover1 = turnover.copy()
turnover1 = np.array(turnover1)   # 数据框转换为list
turnover1 = turnover1.tolist()
turnover2 = np.transpose(turnover1)  # 矩阵转置
turnover2 = pd.DataFrame(turnover2)
turnover2 = turnover2.drop([0])
turnover2.columns = {'1','2','3','4','5','6',
                     '7','8','9','10','11','12'}
turnover2.rename(columns={'8':'1','11':'2','2':'3','6':'4','3':'5','10':'6',
                     '1':'7','4':'8','9':'9','7':'10','5':'11','12':'12'},
           inplace = True) 

turnover2.insert(0,'售货机','')
name = ('A','B','C','D','E') 
turnover2['售货机'] = name

plt.plot(turnover2['售货机'],turnover2['1'])
plt.plot(turnover2['售货机'],turnover2['2'])
plt.plot(turnover2['售货机'],turnover2['3'])
plt.plot(turnover2['售货机'],turnover2['4'])
plt.plot(turnover2['售货机'],turnover2['5'])
plt.plot(turnover2['售货机'],turnover2['6'])
plt.plot(turnover2['售货机'],turnover2['7'])
plt.plot(turnover2['售货机'],turnover2['8'])
plt.plot(turnover2['售货机'],turnover2['9'])
plt.plot(turnover2['售货机'],turnover2['10'])
plt.plot(turnover2['售货机'],turnover2['11'])
plt.plot(turnover2['售货机'],turnover2['12'])
plt.legend(loc= 'center left', bbox_to_anchor=(1,0.5))
# ax1.legend_.remove() 移除子图ax1中的图例
# plt.yticks([0.1,0.15,0.3,0.5,0.7,0.9,1.1])
plt.title("每月各售货机交易额",fontproperties=font)
plt.xlabel("售货机",fontproperties=font)  
plt.ylabel("交易额（元）",fontproperties=font)


# 计算每月总交易额
total = []
for j in range(1,13):
    j = str(j)
    i = sum(turnover2[j])
    total.append(i)

# 计算交易额月环比增长率
totalrate = []
for a in range(1,12):
    c = a-1
    b = total[a] - total[c]
    d = b/total[c]*100
    d = '%.2f' % d
    d = float(d)
    totalrate.append(d)

totalrate1 = pd.DataFrame(totalrate)
totalrate1.columns = {'交易额月环比增长率（%）'}
totalrate1.insert(0,'月份','')
totalrate1['月份'] = range(2,13)
 
# 交易额月环比增长率柱状图
fig = plt.bar(totalrate1['月份'],totalrate1['交易额月环比增长率（%）'])
plt.axhline(y=0.0, c="b", ls="-", lw=1)  # 画参考线
plt.title("交易额月环比增长率柱状图",fontproperties=font)
plt.xlabel("月份",fontproperties=font)  
plt.ylabel("环比增长率(100%)",fontproperties=font)
plt.xticks([2,3,4,5,6,7,8,9,10,11,12])
add_labels(fig)  # 添加数据标签

# 计算总利润
drink = data.loc[ data['大类'] == '饮料']
drinks = sum(drink['实际金额'])
notdrink = data.loc[ data['大类'] == '非饮料']
notdrinks = sum(notdrink['实际金额'])
margins = drinks*0.25 + notdrinks*0.20

# 计算每台售货机毛利润占比
MARGIN = []
MarginRate = []
def margin(data):  
    ddrink = data.loc[ data['大类'] == '饮料']
    ddrinks = sum(ddrink['实际金额'])
    nodrink = data.loc[ data['大类'] == '非饮料']
    nodrinks = sum(nodrink['实际金额'])
    margi = ddrinks*0.25 + nodrinks*0.20
    MARGIN.append(margi)
    d = margi/margins*100
    d = '%.2f' %d
    d = float(d)
    MarginRate.append(d)

margin(A)
margin(B)
margin(C)
margin(D)
margin(E)

mgin = pd.DataFrame(MARGIN)
mginRate = pd.DataFrame(MarginRate)

mgin.columns = {'利润'}
mgin.insert(0,'售货机','')
mgin['售货机'] = name

mginRate.columns = {'利润占比(100%)'}
mginRate.insert(0,'售货机','')
mginRate['售货机'] = name

# 每台售货机毛利润占比饼图
plt.pie(x = mginRate['利润占比(100%)'],labels = mginRate['售货机'],
                      autopct='%.2f%%')
plt.title('每台售货机毛利润占总毛利润的比例',fontproperties=font)

sclass = data.drop_duplicates(['二级类'])
sclas = []
for i in sclass['二级类']:
      sclas.append(i)


# 将索引设置为月份，按月切割     
data = data.drop(columns=['交易时间'])
dat = data.copy()   
dat[['支付时间']] = dat[['支付时间']].astype(str)

t = []
for i in range(0,70679):
    test = dat['支付时间'][i]
    test = test[5:7]
    t.append(test)
    
t = pd.DataFrame(t)
t.columns={'月份'}
dat['月份'] = t['月份']
month1 = dat.loc[dat['月份'] == '01']
month2 = dat.loc[dat['月份'] == '02']
month3 = dat.loc[dat['月份'] == '03']
month4 = dat.loc[dat['月份'] == '04']
month5 = dat.loc[dat['月份'] == '05']
month6 = dat.loc[dat['月份'] == '06']
month7 = dat.loc[dat['月份'] == '07']
month8 = dat.loc[dat['月份'] == '08']
month9 = dat.loc[dat['月份'] == '09']
month10 = dat.loc[dat['月份'] == '10']
month11 = dat.loc[dat['月份'] == '11']
month12 = dat.loc[dat['月份'] == '12']

scalss = dat.drop_duplicates(['二级类']) 

def scla(sc):
    for i in sclass['二级类']:  
        ii = sc.loc[sc['二级类'] ==  i]
        money = sum(ii['实际金额'])
        aver.append(money)
 
aver = []       
scla(month1)  
aver1 = pd.DataFrame(aver)
aver1.columns={'1月交易额'}

aver = []
scla(month2)
aver2 = pd.DataFrame(aver)
aver2.columns={'2月交易额'}

aver = []
scla(month3)
aver3 = pd.DataFrame(aver)
aver3.columns={'3月交易额'}

aver = []
scla(month4)
aver4 = pd.DataFrame(aver)
aver4.columns={'4月交易额'}

aver = []
scla(month5)
aver5 = pd.DataFrame(aver)
aver5.columns={'5月交易额'}

aver = []
scla(month6)
aver6 = pd.DataFrame(aver)
aver6.columns={'6月交易额'}
sum(aver6['交易额'])

aver = []
scla(month7)
aver7 = pd.DataFrame(aver)
aver7.columns={'7月交易额'}

aver = []
scla(month8)
aver8 = pd.DataFrame(aver)
aver8.columns={'8月交易额'}

aver = []
scla(month9)
aver9 = pd.DataFrame(aver)
aver9.columns={'9月交易额'}

aver = []
scla(month10)
aver10 = pd.DataFrame(aver)
aver10.columns={'10月交易额'}

aver = []
scla(month11)
aver11 = pd.DataFrame(aver)
aver11.columns={'11月交易额'}

aver = []
scla(month12)
aver12 = pd.DataFrame(aver)
aver12.columns={'12月交易额'}

# 数据框拼接，axis = 1 表示列拼接
dfaver = pd.concat( [aver1,aver2,aver3,
                     aver4,aver5,aver6,aver7,aver8,aver9,
                     aver10,aver11,aver12], axis=1 )
    
dfaver.insert(0,'二级类','')
bb = sclass['二级类']
bb = pd.DataFrame(bb)
bb['m'] = range(0,20)
bb = bb.set_index('m')
dfaver['二级类'] = bb
# dfaver = dfaver.drop(columns = '二级类商品')
dfaver.to_csv("E:/Vending machine1/每月二级商品交易额.csv",
         sep=",",index=False,header=True)

# 数据框拼接，axis = 1 表示列拼接
dfaver = pd.concat( [aver1,aver2,aver3,
                     aver4,aver5,aver6,aver7,aver8,aver9,
                     aver10,aver11,aver12], axis=1 )
    
dfaver.insert(0,'二级类','')
bb = sclass['二级类']
bb = pd.DataFrame(bb)
bb['m'] = range(0,20)
bb = bb.set_index('m')
dfaver['二级类'] = bb
# scg = scg.drop(columns = 'Unnameed:13')
dfaver.to_csv("E:/Vending machine1/每月二级商品订单量.csv",
         sep=",",index=False,header=True)

scgood = pd.read_csv("每月二级商品单均额.csv",sep = ',' ,encoding = 'gbk')

# 气泡图
size1=scgood['1月单均额'].rank()
size2=scgood['2月单均额'].rank()
size3=scgood['3月单均额'].rank()
size4=scgood['4月单均额'].rank()
size5=scgood['5月单均额'].rank()
size6=scgood['6月单均额'].rank()
size7=scgood['7月单均额'].rank()
size8=scgood['8月单均额'].rank()
size9=scgood['9月单均额'].rank()
size10=scgood['10月单均额'].rank()
size11=scgood['11月单均额'].rank()
size12=scgood['12月单均额'].rank()
n=20
plt.rcParams['font.sans-serif']=['SimHei']
plt.scatter(scgood['二级类'],scgood['1月单均额'],
            s=size1*n,alpha=0.6)
plt.scatter(scgood['二级类'],scgood['2月单均额'],
            s=size2*n,alpha=0.6)
plt.scatter(scgood['二级类'],scgood['3月单均额'],
            s=size3*n,alpha=0.6)
plt.scatter(scgood['二级类'],scgood['4月单均额'],
            s=size4*n,alpha=0.6)
plt.scatter(scgood['二级类'],scgood['5月单均额'],
            s=size5*n,alpha=0.6)
plt.scatter(scgood['二级类'],scgood['6月单均额'],
            s=size6*n,alpha=0.6)
plt.scatter(scgood['二级类'],scgood['7月单均额'],
            s=size7*n,alpha=0.6)
plt.scatter(scgood['二级类'],scgood['8月单均额'],
            s=size8*n,alpha=0.6)
plt.scatter(scgood['二级类'],scgood['9月单均额'],
            s=size9*n,alpha=0.6)
plt.scatter(scgood['二级类'],scgood['10月单均额'],
            s=size10*n,alpha=0.6)
plt.scatter(scgood['二级类'],scgood['11月单均额'],
            s=size11*n,alpha=0.6)
plt.scatter(scgood['二级类'],scgood['12月单均额'],
            s=size12*n,alpha=0.6)
plt.grid(axis="x")
plt.title("二级商品交易额均值",fontproperties=font)
plt.ylabel("交易额均值",fontproperties=font)
plt.xlabel("二级商品",fontproperties=font)
pl.xticks(rotation = 30)  # x轴刻度倾斜
plt.legend(loc= 'center left', bbox_to_anchor=(1,0.5))



