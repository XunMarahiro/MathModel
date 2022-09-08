# -*- coding:utf-8 -*-
import pandas as pd
import math
data1=pd.read_excel('附件1处理过后数据.xlsx').set_index("索引")
data=pd.DataFrame(columns=['公司名称','借贷额度','预计利润','利率'])
data1_In=123
profile_Sum=0
out_sum=0
for i in range(0,data1_In):
    name=data1.iloc[i,0]
    In_Sum=data1.iloc[i,1]
    In_times=data1.iloc[i,2]
    Out_Sum=data1.iloc[i,3]
    Out_times=data1.iloc[i,4]
    profit=data1.iloc[i,5]
    profit_In=data1.iloc[i,6]
    label1=data1.iloc[i,7]
    label2=data1.iloc[i,8]
    profit_rate=data1.iloc[i,9]
    if profit_rate==0:
        data.loc[len(data.index)] = [name, 0, 0, 0]
    else:
        a=(abs(In_Sum)+abs(Out_Sum))*0.1
        if a>1000000:
            a=1000000
        if a<100000:
            a=100000
        data.loc[len(data.index)] = [name,a,a*profit_rate,profit_rate]
        profile_Sum=profile_Sum+a*profit_rate
        out_sum=out_sum+a
print(data)
print(profile_Sum)
print(out_sum)

writer = pd.ExcelWriter('结果.xlsx')
data.to_excel(writer)
writer.save()