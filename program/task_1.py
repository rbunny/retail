import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime
from scipy import stats 
from pandas.core.frame import DataFrame
import matplotlib.font_manager as font_manager
font = font_manager.FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf")
font.set_size(12)

# 读取附件中的数据
data1 = pd.read_csv("附件1.csv",sep = ',' ,encoding = 'gbk')
data2 = pd.read_csv("附件2.csv",sep = ',' ,encoding = 'gbk')

# ----- 数据预处理 -------

# 检查缺失值
data1.isnull().any()   # 获取含有缺失值的列
data2.isnull().any()

# 检查各列
data1.loc[data1['实际金额']!=data1['应付金额']]
data1.loc[data1['状态']!='已出货未退款']
data1.loc[data1['提现']!='已提现']

# 删除不必要的列,inplace=True 表示删除操作改变原数据
data1.drop(["订单号","设备ID","状态","提现"],axis=1,inplace=True)
data1.drop(["应付金额"],axis=1,inplace=True)

# 检查时间
data1['支付时间'] = pd.to_datetime(data1['支付时间'])
data1 = data1.drop([70679])   # 删除错误数据

# 数据可视化
plt.plot(data1['实际金额'])   # 检查商品价格
plt.title("实际金额",fontproperties=font)
plt.ylabel("价格（元）",fontproperties=font)

b = data1.loc[data1['商品'] == '旺仔牛奶']
b1 = data1.loc[data1['商品']=='100g*5瓶益力多']
b2 = data1.loc[data1['商品']=='145ml旺仔牛奶盒装']
b3 = data1.loc[data1['商品'] == '营养快线']

# 一表多图
plt.subplot(2,2,1)
plt.plot(b['实际金额'])
plt.title("旺仔牛奶",fontproperties=font)
plt.ylabel("价格（元）",fontproperties=font)

plt.subplot(2,2,2)
plt.plot(b1['实际金额'])
plt.title("100g*5瓶益力多",fontproperties=font)
plt.ylabel("价格（元）",fontproperties=font)

plt.subplot(2,2,3)
plt.plot(b2['实际金额'])
plt.title("145ml旺仔牛奶盒装",fontproperties=font)
plt.ylabel("价格（元）",fontproperties=font)

plt.subplot(2,2,4)
plt.plot(b3['实际金额'])
plt.title("营养快线",fontproperties=font)
plt.ylabel("价格（元）",fontproperties=font)


#  提取商品价格
good = data1.drop_duplicates(['商品'])   # 数据的某一列去重

ee = []
for i in good['商品']:
      ee.append(i)
    
bb = []
for i in range(0,303):
    b = data1.loc[data1['商品']== ee[i]]
    d = stats.mode(b['实际金额'])[0][0]    # 求众数
    bb.append(d)

ee = pd.DataFrame(ee)
ee.columns = {'商品'}   # 直接修改列名
ee['商品价格'] = bb

plt.plot(ee['商品价格'])

# 检查高价格商品
goodprice = ee.loc[ee['商品价格']>15]
goodprice = goodprice.set_index('商品')
plt.plot(goodprice['商品价格'],marker='o')
plt.grid(axis = 'y')
plt.title("高价格商品图",fontproperties=font)
plt.ylabel("价格（元）",fontproperties=font)
plt.xticks(fontproperties=font, rotation = 10)  # x轴显示中文

ee.to_csv("E:/Vending machine1/商品价格.csv",
         sep=",",index=False,header=True)


# 更正价格
dataa = data1.copy()     # 复制才不会修改原数据
dat = np.array(dataa)   # 数据框转换为list
dat = dat.tolist()
g = np.array(good)
g = g.tolist()

for i in range(0,303):  
    for j in range(0,70679):
        if dat[j][1] == g[i][0]:
            dat[j][0] = g[i][1]
        else:
            continue
        
dat1 = pd.DataFrame(dat) 

# 检查是否修复       
plt.plot(dat1['实际金额'])
plt.title("修改后的实际金额",fontproperties=font)
plt.ylabel("价格（元）",fontproperties=font)

plt.plot(good['商品价格'])

dat1.rename(columns={'支付时间':'商品','地点':'支付时间','商品':'地点'},
           inplace = True)    #  修改列名
dat1.to_csv("E:/Vending machine1/价格更正.csv",
         sep=",",index=False,header=True)

# 合并数据，商品类别
dat1.insert(2,'大类','')   # 在第三列前插入一列
dat1.insert(3,'二级类','')

dat2 = np.array(dat1)
dat2 = dat2.tolist()
data2 = np.array(data1)
data2 = data2.tolist()

for i in range(0,315):  
    for j in range(0,70679):
        if dat2[j][1] == data2[i][0]:
            dat2[j][2] = data2[i][1]
            dat2[j][3] = data2[i][2]
        else:
            continue
   
     
dat2 = pd.DataFrame(dat2) 
dat2.columns = {'实际金额','商品','大类','二级类','支付时间','地点'}
dat2.rename(columns={'大类':'实际金额','支付时间':'商品',
            '实际金额':'大类','地点':'二级类','商品':'支付时间',
            '二级类':'地点'},
            inplace = True)    

dat2.to_csv("E:/Vending machine1/最终数据.csv",
         sep=",",index=False,header=True)


#  提取每台售货机的数据

A = data.loc[data['地点']=='A']
B = data.loc[data['地点']=='B']
C = data.loc[data['地点']=='C']
D = data.loc[data['地点']=='D']
E = data.loc[data['地点']=='E']

# 导出每台售货机的数据

A.to_csv("E:/Vending machine1/task1-1A.csv",
         sep=",",index=False,header=True)
B.to_csv("E:/Vending machine1/task1-1B.csv",
         sep=",",index=False,header=True)
C.to_csv("E:/Vending machine1/task1-1C.csv",
         sep=",",index=False,header=True)
D.to_csv("E:/Vending machine1/task1-1D.csv",
         sep=",",index=False,header=True)
E.to_csv("E:/Vending machine1/task1-1E.csv",
         sep=",",index=False,header=True)

# 提取5月份的数据
def selectMonth5(AA):
    AA['交易时间'] = AA['支付时间']
    AA['支付时间'] = pd.to_datetime(AA['支付时间'])  
    AA = AA.set_index('支付时间') 
    acopy = AA['2017-5-1':'2017-5-31']
    return acopy

A5 = selectMonth5(A)
B5 = selectMonth5(B)
C5 = selectMonth5(C)
D5 = selectMonth5(D)
E5 = selectMonth5(E)

# 计算5月份的交易额、订单量，交易总额和订单总量
def sumturnover(a):
    aa = sum(a['实际金额'])
    return aa

sumA5 = sumturnover(A5)
sumB5 = sumturnover(B5)
sumC5 = sumturnover(C5)
sumD5 = sumturnover(D5)
sumE5 = sumturnover(E5)

# 计算订单量
Alen = len(A5)
Blen = len(B5)
Clen = len(C5)
Dlen = len(D5)
Elen = len(E5)








