# -*- coding:utf-8 -*-
import math
from sklearn import preprocessing
import matplotlib.pyplot as plt
import numpy as np
from sklearn import  svm,datasets
import pandas as pd
from sklearn import model_selection
import pickle #pickle模块
from sklearn.preprocessing import RobustScaler

with open('save/clf.pickle', 'rb') as f:
    clf = pickle.load(f)

data=pd.DataFrame(columns=['x','x','x','x','x','x','x','x','x'])
data1=pd.read_excel('傻逼数据.xlsx',sheet_name="Sheet3")
name_list=pd.DataFrame(columns=['公司编号'])
data1_In=123
data2_In=300
for i in range(0,302):
    name=data1.iloc[i,0]
    In_Sum=data1.iloc[i,1]
    In_times=data1.iloc[i,2]
    Out_Sum=data1.iloc[i,3]
    Out_times=data1.iloc[i,4]
    profit=data1.iloc[i,5]
    profit_In=data1.iloc[i,6]
    No_Use = data1.iloc[i, 7]
    Sum_Time = data1.iloc[i, 8]
    No_Times = data1.iloc[i, 9]
    # big_10=data1.iloc[i,10]
    # profit_all=data1.iloc[i,11]
    # In_rate = data1.iloc[i, 12]
    # Out_rate = data1.iloc[i, 13]
    # Up = data1.iloc[i, 14]
    # Down = data1.iloc[i, 15]
    data.loc[len(data.index)] = [In_Sum,In_times,Out_Sum,Out_times,profit,profit_In,No_Use,Sum_Time,No_Times]
    name_list.loc[len(name_list.index)]=[name]
data=RobustScaler().fit(data).transform(data)
print(data)
a=pd.DataFrame(clf.predict(data))
print(a)
b=1/(1+np.exp(-clf.decision_function(data)*5))
print(clf.decision_function(data))
b=pd.DataFrame(b)
result=pd.concat([name_list,a,b], axis=1, ignore_index=True)
# result=pd.concat([result,b], axis=1, ignore_index=True)


writer = pd.ExcelWriter('预测结果.xlsx')
result.to_excel(writer)
writer.save()