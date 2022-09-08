# -*- coding: utf-8 -*-
"""MyProblem.py"""
import numpy as np
import geatpy as ea
from sklearn import svm
from sklearn import preprocessing
from sklearn.model_selection import cross_val_score
from multiprocessing.dummy import Pool as ThreadPool


class MyProblem(ea.Problem):  # 继承Problem父类
    def __init__(self):
        name = 'MyProblem'  # 初始化name（函数名称，可以随意设置）
        M = 1  # 初始化M（目标维数）
        maxormins = [-1]  # 初始化maxormins（目标最小最大化标记列表，1：最小化该目标；-1：最大化该目标）
        Dim = 2  # 初始化Dim（决策变量维数）
        varTypes = [0, 0]  # 初始化varTypes（决策变量的类型，元素为0表示对应的变量是连续的；1表示是离散的）
        lb = [2 ** (-8)] * Dim  # 决策变量下界
        ub = [2 ** 8] * Dim  # 决策变量上界
        lbin = [1] * Dim  # 决策变量下边界（0表示不包含该变量的下边界，1表示包含）
        ubin = [1] * Dim  # 决策变量上边界（0表示不包含该变量的上边界，1表示包含）
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)
        # 目标函数计算中用到的一些数据
        fp = open('iris_train.data')
        datas = []
        data_targets = []
        for line in fp.readlines():
            line_data = line.strip('\n').split(',')
            data = []
            for i in line_data[0:4]:
                data.append(float(i))
            datas.append(data)
            data_targets.append(line_data[4])
        fp.close()
        self.data = preprocessing.scale(np.array(datas))  # 训练集的特征数据（归一化）
        self.dataTarget = np.array(data_targets)

    def aimFunc(self, pop):  # 目标函数，采用多线程加速计算
        Vars = pop.Phen  # 得到决策变量矩阵
        pop.ObjV = np.zeros((pop.sizes, 1))  # 初始化种群个体目标函数值列向量

        def subAimFunc(i):
            C = Vars[i, 0]
            G = Vars[i, 1]
            svc = svm.SVC(C=C, kernel='rbf', gamma=G).fit(self.data, self.dataTarget)  # 创建分类器对象并用训练集的数据拟合分类器模型
            scores = cross_val_score(svc, self.data, self.dataTarget, cv=10)  # 计算交叉验证的得分
            pop.ObjV[i] = scores.mean()  # 把交叉验证的平均得分作为目标函数值

        pool = ThreadPool(2)  # 设置池的大小
        pool.map(subAimFunc, list(range(pop.sizes)))

    def test(self, C, G):  # 代入优化后的C、Gamma对测试集进行检验
        # 读取测试集数据
        fp = open('iris_test.data')
        datas = []
        data_targets = []
        for line in fp.readlines():
            line_data = line.strip('\n').split(',')
            data = []
            for i in line_data[0:4]:
                data.append(float(i))
            datas.append(data)
            data_targets.append(line_data[4])
        fp.close()
        data_test = preprocessing.scale(np.array(datas))  # 测试集的特征数据（归一化）
        dataTarget_test = np.array(data_targets)  # 测试集的标签数据
        svc = svm.SVC(C=C, kernel='rbf', gamma=G).fit(self.data, self.dataTarget)  # 创建分类器对象并用训练集的数据拟合分类器模型
        dataTarget_predict = svc.predict(data_test)  # 采用训练好的分类器对象对测试集数据进行预测
        print("测试集数据分类正确率 = %s%%" % (
                    len(np.where(dataTarget_predict == dataTarget_test)[0]) / len(dataTarget_test) * 100))