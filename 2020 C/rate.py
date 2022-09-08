# -*- coding:utf-8 -*-
import math
import pandas as pd

rate_list=pd.DataFrame(columns=['利率'])
def line(rate):
    return -1.121483610782915 + 37.96951967720239 * rate + -258.5704506433328 * rate*rate + 640.9444234563296 * rate*rate*rate



def tree(bad_rate):
    step=0.00001
    val=0.04
    worth_max=0
    val_max=0
    while val<=0.15:
        field=line(val)
        earn=(1-bad_rate)*val-bad_rate
        worth=earn*(1-field)
        if worth>worth_max:
            worth_max=worth
            val_max=val
        val=val+step
    rate_list.loc[len(rate_list.index)] = [val_max]

data=pd.read_excel('预测结果.xlsx').set_index('Unnamed: 0')
print(data.loc[:,2].values)
loss_rate=data.loc[:,2].values
for i in loss_rate:
    tree(i)
result=pd.concat([data,rate_list], axis=1, ignore_index=True)

writer = pd.ExcelWriter('save.xlsx')
result.to_excel(writer)
writer.save()
print(result)