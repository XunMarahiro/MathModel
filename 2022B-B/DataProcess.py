import math
import random

import pandas as pd


def plane_add(data, index, code, now_loc, pre_loc, state):
    data.loc[index, '编号'] = code
    data.loc[index, '当前位置'] = now_loc
    data.loc[index, '目标位置'] = pre_loc
    data.loc[index, '预测位置'] = [0, 0]
    data.loc[index, '上次位置'] = now_loc
    data.loc[index, '状态'] = state
    data.loc[index, '位移标量'] = 0
    data.loc[index, '位移量'] = [0, 0]
    data.loc[index, '运行步数'] = str(0)
    data.loc[0, '目标标量'] = 0
    loc_t = now_loc
    if loc_t[1] == 0:
        loc_t[1] = 1
    data.loc[index, '原点方向量'] = loc_t[0] / loc_t[1]


class Database:
    def __init__(self, now_loc, pre_loc):
        self.Data = pd.DataFrame(
            {'编号': 'E0', '上次位置': '[0,0]', '当前位置': '[0.0]', '预测位置': '[0,0]', '目标位置': '[0,0]',
             '位移量': '[0,0]',
             '状态': 'mother', '位移标量': '', '原点方向量': '', '运行步数': '0', '目标标量': ''}, index=[0])
        self.Data.loc[0, '当前位置'] = [0, 0]
        self.Data.loc[0, '目标位置'] = [0, 0]
        self.Data.loc[0, '预测位置'] = [0, 0]
        self.Data.loc[0, '位移量'] = [0, 0]
        self.Data.loc[0, '位移标量'] = 0
        self.Data.loc[0, '运行步数'] = 0
        self.Data.loc[0, '位移标量'] = 0
        self.Data.loc[0, '目标标量'] = 0
        for i in range(0, len(now_loc)):
            code = 'E' + str(i + 1)
            plane_add(self.Data, i + 1, code, now_loc[i], pre_loc[i], 'none')

    def Get_Mother(self):
        val_min = 100
        less = []
        val = []
        for i in range(0, len(self.Data)):
            now_loc = self.Data.loc[i, '当前位置']
            loc_t = now_loc
            if loc_t[1] == 0:
                loc_t[1] = 1
            self.Data.loc[i, '原点方向量'] = loc_t[0] / loc_t[1]
            val.append(self.Data.loc[i, '原点方向量'])
        self.Data.loc[1:, "状态"] = 'none'
        for a in range(1, len(self.Data)):
            pre_loc = self.Data.loc[a, '当前位置']
            tar_loc = self.Data.loc[a, '目标位置']
            move_sum = [tar_loc[0] - pre_loc[0], tar_loc[1] - pre_loc[1]]
            va = math.sqrt(math.pow(move_sum[0], 2) + math.pow(move_sum[1], 2))
            self.Data.loc[a, '目标标量'] = va
        self.Data=self.Data.sort_values(by='目标标量').reset_index().drop('index', axis=1)

        for i in range(0, len(self.Data)):
            now_loc = self.Data.loc[i, '当前位置']
            loc_t = now_loc
            if loc_t[1] == 0:
                loc_t[1] = 1
            self.Data.loc[i, '原点方向量'] = loc_t[0] / loc_t[1]
            val.append(self.Data.loc[i, '原点方向量'])
        self.Data.loc[1:, "状态"] = 'none'
        b=len(self.Data[self.Data['目标标量']<10])
        if b <4:
            b=5
        print(self.Data)
        while self.Data['状态'].value_counts()['mother'] != 4:
            val_t = val
            a = random.randint(1, b-1)
            print(a,b)
            tar = self.Data.loc[a, '原点方向量']
            if tar in val_t:
                val_t.remove(self.Data.loc[a, '原点方向量'])

            Flag = 1
            for i in val_t:
                if i + 0.1 > tar and i - 0.1 < tar:
                    Flag = 0
            if Flag:
                    self.Data.loc[a, '状态'] = 'mother'
                    self.Data.loc[a, '位移量'] = [0, 0]
                    self.Data.loc[a, '预测位置'] = [0, 0]

    def Mother_Moving(self, Time, A):
        print(Time % 5, Time)
        if Time % 5 == 0:
            self.Data.loc[0, '当前位置'] = [self.Data.loc[0, '当前位置'][0] + A[0],
                                            self.Data.loc[0, '当前位置'][1] + A[1]]
            self.Data.loc[0, '目标位置'] = [self.Data.loc[0, '目标位置'][0] + A[0],
                                            self.Data.loc[0, '目标位置'][1] + A[1]]
            for i in range(1, len(self.Data)):
                self.Data.loc[i, '目标位置'] = [self.Data.loc[i, '目标位置'][0] + A[0],
                                                self.Data.loc[i, '目标位置'][1] + A[1]]
