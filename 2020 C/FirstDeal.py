# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib as plt
import matplotlib

result=pd.DataFrame(columns=['公司代号','进项总金额','进项交易总次数','销项总金额','销项交易总次数'])
data1_In=210946
data1_Out=162483
data2_In=395174
data2_Out=330834
filename='data2.xlsx'
data1=pd.read_excel(filename,sheet_name='进项发票信息')
for i in range(0,data2_In):
    val=data1.iloc[i]
    name=val.iloc[0]
    amount=val.iloc[6]
    state=val.iloc[7]
    print(i)
    if state=='有效发票':
        try:
            val = int(result[result.公司代号 == name].index.tolist()[0])
        except:
            result.loc[len(result.index)] = [name, 0, 0,0,0]
        val = int(result[result.公司代号 == name].index.tolist()[0])
        result.iloc[val, 1] = result.iloc[val, 1] + amount
        result.iloc[val, 2]=  result.iloc[val, 2]+1

data1=pd.read_excel(filename,sheet_name='销项发票信息')
for i in range(0,data2_Out):
    val=data1.iloc[i]
    name=val.iloc[0]
    amount=val.iloc[6]
    state=val.iloc[7]
    print(i)
    if state=='有效发票':
        try:
            val = int(result[result.公司代号 == name].index.tolist()[0])
            result.iloc[val, 3] = result.iloc[val, 3] + amount
            result.iloc[val, 4]=  result.iloc[val, 4]+1
        except:
            print(name)
            break

writer = pd.ExcelWriter('save.xlsx')
result.to_excel(writer)
writer.save()