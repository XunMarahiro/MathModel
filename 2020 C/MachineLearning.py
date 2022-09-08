# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from sklearn import  svm,datasets
import pandas as pd
from sklearn import model_selection
import pickle #pickle模块
from sklearn.preprocessing import RobustScaler
data=pd.DataFrame(columns=['x','x','x','x','x','x','x','x','x','y'])
data1=pd.read_excel('傻逼数据.xlsx',sheet_name='Sheet2')

data1_In=300
for i in range(0,302):
    In_Sum=data1.iloc[i,1]
    In_times=data1.iloc[i,2]
    Out_Sum=data1.iloc[i,3]
    Out_times=data1.iloc[i,4]
    profit=data1.iloc[i,5]
    profit_In=data1.iloc[i,6]
    label1=data1.iloc[i,7]
    label2=data1.iloc[i,8]
    Data_9=data1.iloc[i,9]
    No_Use=data1.iloc[i,10]
    # time_rate=data1.iloc[i,11]
    # label1_bool=data1.iloc[i,12]
    # big_10=data1.iloc[i,13]
    # profit_all=data1.iloc[i,14]
    # In_rate = data1.iloc[i, 15]
    # Out_rate = data1.iloc[i, 16]
    # Up = data1.iloc[i, 17]
    # Down = data1.iloc[i, 18]
    data.loc[len(data.index)] = [In_Sum,In_times,Out_Sum,Out_times,profit,profit_In,label1,label2,Data_9,No_Use]

x,y=np.split(data,(9,),axis=1)
x=RobustScaler().fit(x).transform(x)
y=y.values
print(x)
print(y)
x_train,x_test,y_train,y_test=model_selection.train_test_split(x,y,random_state=4,test_size=0.2)


classifier=svm.SVC(kernel='rbf',gamma=0.001,decision_function_shape='ovo',C=300)
classifier.fit(x_train,y_train.ravel())

def show_accuracy(y_hat,y_train,str):
    pass


#（4）计算svm分类器的准确率
print("SVM-输出训练集的准确率为：",classifier.score(x_train,y_train))
y_hat=classifier.predict(x_train)
show_accuracy(y_hat,y_train,'训练集')
print("SVM-输出测试集的准确率为：",classifier.score(x_test,y_test))

y_hat=classifier.predict(x_test)
show_accuracy(y_hat,y_test,'测试集')
# SVM-输出训练集的准确率为： 0.838095238095
# SVM-输出测试集的准确率为： 0.777777777778


# 查看决策函数，可以通过decision_function()实现。decision_function中每一列的值代表距离各类别的距离。

# print('decision_function:\n', classifier.decision_function(x_train))
# print('\npredict:\n', classifier.predict(x_train))

with open('save/clf.pickle', 'wb') as f:
    pickle.dump(classifier,f)

