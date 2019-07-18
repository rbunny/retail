# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 11:40:11 2019

@author: asus
"""
import pylab as pl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
import seaborn as sns
from pandas.core.frame import DataFrame
import matplotlib.font_manager as font_manager
font = font_manager.FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf")
font.set_size(12)

A = pd.read_csv("A/task1-1A.csv",sep = ',' ,encoding = 'utf-8')
B = pd.read_csv("B/task1-1B.csv",sep = ',' ,encoding = 'utf-8')
C = pd.read_csv("C/task1-1C.csv",sep = ',' ,encoding = 'utf-8')
D = pd.read_csv("D/task1-1D.csv",sep = ',' ,encoding = 'utf-8')
E = pd.read_csv("E/task1-1E.csv",sep = ',' ,encoding = 'utf-8')

aa = A['商品'].value_counts()
a1 = pd.concat( [A['商品'],A['实际金额']], axis=1 )
a1 = a1.drop_duplicates(['商品'])
a1 = a1.set_index(['商品'])
a1['数量'] = aa
a3 = aa/52
for i in range(0,274):
    a3[i] = int(a3[i])
a1['周均销量'] = a3

a4 = aa/12
for i in range(0,274):
    a4[i] = int(a4[i])
a1['月均销量'] = a4

a6 = []
for i in a1.index:
    if a1['周均销量'][i]!=0:
        a5 = '热销'
    else:
        if a1['月均销量'][i]!=0:
            a5 = '平销'
        elif a1['月均销量'][i]==0:
            a5 = '滞销'
    a6.append(a5)
a1['商品标签'] = a6 
A = A.set_index(['商品'])
A['商品标签'] = a1['商品标签']

b = B['商品'].value_counts()
b1 = pd.concat( [B['商品'],B['实际金额']], axis=1 )
b1 = b1.drop_duplicates(['商品'])
b1 = b1.set_index(['商品'])
b1['数量'] = b
b3 = b/52
for i in range(0,len(b3)):
    b3[i] = int(b3[i])
b1['周均销量'] = b3

b4 = b/12
for i in range(0,len(b4)):
    b4[i] = int(b4[i])
b1['月均销量'] = b4

b6 = []
for i in b1.index:
    if b1['周均销量'][i]!=0:
        b5 = '热销'
    else:
        if b1['月均销量'][i]!=0:
            b5 = '平销'
        elif b1['月均销量'][i]==0:
            b5 = '滞销'
    b6.append(b5)
b1['商品标签'] = b6
B = B.set_index(['商品'])
B['商品标签'] = b1['商品标签']

c = C['商品'].value_counts()
c1 = pd.concat( [C['商品'],C['实际金额']], axis=1 )
c1 = c1.drop_duplicates(['商品'])
c1 = c1.set_index(['商品'])
c1['数量'] = c
c3 = c/52
for i in range(0,len(c3)):
    c3[i] = int(c3[i])
c1['周均销量'] = c3

c4 = c/12
for i in range(0,len(c4)):
    c4[i] = int(c4[i])
c1['月均销量'] = c4

c6 = []
for i in c1.index:
    if c1['周均销量'][i]!=0:
        c5 = '热销'
    else:
        if c1['月均销量'][i]!=0:
            c5 = '平销'
        elif c1['月均销量'][i]==0:
            c5 = '滞销'
    c6.append(c5)
c1['商品标签'] = c6 
C = C.set_index(['商品'])
C['商品标签'] = c1['商品标签']


d = D['商品'].value_counts()
d1 = pd.concat( [D['商品'],D['实际金额']], axis=1 )
d1 = d1.drop_duplicates(['商品'])
d1 = d1.set_index(['商品'])
d1['数量'] = d
d3 = d/52
for i in range(0,len(d3)):
    d3[i] = int(d3[i])
d1['周均销量'] = d3

d4 = d/12
for i in range(0,len(d4)):
    d4[i] = int(d4[i])
d1['月均销量'] = d4

d6 = []
for i in d1.index:
    if d1['周均销量'][i]!=0:
        d5 = '热销'
    else:
        if d1['月均销量'][i]!=0:
            d5 = '平销'
        elif d1['月均销量'][i]==0:
            d5 = '滞销'
    d6.append(d5)
d1['商品标签'] = d6 
D = D.set_index(['商品'])
D['商品标签'] = d1['商品标签']


e = E['商品'].value_counts()
e1 = pd.concat( [E['商品'],E['实际金额']], axis=1 )
e1 = e1.drop_duplicates(['商品'])
e1 = e1.set_index(['商品'])
e1['数量'] = e
e3 = e/52
for i in range(0,len(e3)):
    e3[i] = int(e3[i])
e1['周均销量'] = e3

e4 = e/12
for i in range(0,len(e4)):
    e4[i] = int(e4[i])
e1['月均销量'] = e4

e6 = []
for i in e1.index:
    if e1['周均销量'][i]!=0:
        e5 = '热销'
    else:
        if e1['月均销量'][i]!=0:
            e5 = '平销'
        elif e1['月均销量'][i]==0:
            e5 = '滞销'
    e6.append(e5)
e1['商品标签'] = e6 
E = E.set_index(['商品'])
E['商品标签'] = e1['商品标签']

A.to_csv("E:/Vending machine1/task3_1A.csv",
         sep=",",index=True,header=True)
B.to_csv("E:/Vending machine1/task3_1B.csv",
         sep=",",index=True,header=True)
C.to_csv("E:/Vending machine1/task3_1C.csv",
         sep=",",index=True,header=True)
D.to_csv("E:/Vending machine1/task3_1D.csv",
         sep=",",index=True,header=True)
E.to_csv("E:/Vending machine1/task3_1E.csv",
         sep=",",index=True,header=True)

a1.to_csv("E:/Vending machine1/task3a.csv",
         sep=",",index=True,header=True)
b1.to_csv("E:/Vending machine1/task3b.csv",
         sep=",",index=True,header=True)
c1.to_csv("E:/Vending machine1/task3c.csv",
         sep=",",index=True,header=True)
d1.to_csv("E:/Vending machine1/task3d.csv",
         sep=",",index=True,header=True)
e1.to_csv("E:/Vending machine1/task3e.csv",
         sep=",",index=True,header=True)

A = pd.read_csv("task3_1A.csv",sep = ',' ,encoding = 'utf-8')
B = pd.read_csv("task3_1B.csv",sep = ',' ,encoding = 'utf-8')
C = pd.read_csv("task3_1C.csv",sep = ',' ,encoding = 'utf-8')
D = pd.read_csv("task3_1D.csv",sep = ',' ,encoding = 'utf-8')
E = pd.read_csv("task3_1E.csv",sep = ',' ,encoding = 'utf-8')

A = A.drop_duplicates(['商品'])
B = B.drop_duplicates(['商品'])
C = C.drop_duplicates(['商品'])
D = D.drop_duplicates(['商品'])
E = E.drop_duplicates(['商品'])

A1 = A.loc[A['商品标签'] == '热销']
A2 = A.loc[A['商品标签'] == '平销']
A3 = A.loc[A['商品标签'] == '滞销']

B1 = B.loc[B['商品标签'] == '热销']
B2 = B.loc[B['商品标签'] == '平销']
B3 = B.loc[B['商品标签'] == '滞销']

C1 = C.loc[C['商品标签'] == '热销']
C2 = C.loc[C['商品标签'] == '平销']
C3 = C.loc[C['商品标签'] == '滞销']

D1 = D.loc[D['商品标签'] == '热销']
D2 = D.loc[D['商品标签'] == '平销']
D3 = D.loc[D['商品标签'] == '滞销']

E1 = E.loc[E['商品标签'] == '热销']
E2 = E.loc[E['商品标签'] == '平销']
E3 = E.loc[E['商品标签'] == '滞销']

D1.to_csv("E:/Vending machine1/D热销.csv",
         sep=",",index=False,header=True)
D2.to_csv("E:/Vending machine1/D平销.csv",
         sep=",",index=False,header=True)
D3.to_csv("E:/Vending machine1/D滞销.csv",
         sep=",",index=False,header=True)

E1.to_csv("E:/Vending machine1/E热销.csv",
         sep=",",index=False,header=True)
E2.to_csv("E:/Vending machine1/E平销.csv",
         sep=",",index=False,header=True)
E3.to_csv("E:/Vending machine1/E滞销.csv",
         sep=",",index=False,header=True)
