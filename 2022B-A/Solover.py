from math import sqrt, pow, acos, pi, fabs

import matplotlib.pyplot as plt
import pandas as pd

step = 0.01
S = 0.5
backemf = -int(S/step)


def length(a, b):
    return sqrt(abs(pow(a[1] - b[1], 2) + pow(a[0] - b[0], 2)))


def angel(a, b, c):
    A = length(b, c)
    B = length(a, c)
    C = length(a, b)
    val = (pow(A, 2) + pow(B, 2) - pow(C, 2)) / (2 * A * B)
    if val < -1 or val > 1:
        return 0
    return acos(val) / pi * 180


def solover(a, b, c, d, c1, c2, c3, c4, v):
    if v == a or v == b or v == c or v == d:
        return 10
    else:
        A = angel(a, b, v)
        B = angel(b, c, v)
        C = angel(c, d, v)
        D = angel(d, a, v)
        return fabs(A - c1) + fabs(B - c2) + fabs(C - c3) + fabs(D - c4)


def FindAngle(a, b, c, d, v):
    A = angel(a, b, v)
    B = angel(b, c, v)
    C = angel(c, d, v)
    D = angel(d, a, v)
    return A, B, C, D


def findpoint(a, b, c, d, c1, c2, c3, c4, v,nomather,mother):

    return minix


def get_location(a, b, c, d, v,nomather,mother):
    c1, c2, c3, c4 = FindAngle(a, b, c, d, v)
    return findpoint(a, b, c, d, c1, c2, c3, c4, v,nomather,mother)


def Moving(Data):
    for i in range(0,len(Data)):
        now_loc=Data.loc[i,'当前位置']
        Data.loc[i,'上次位置']=now_loc
        pre_loc = Data.loc[i, '预测位置']
        tar_loc = Data.loc[i, '目标位置']
        move_val = [tar_loc[0] - pre_loc[0], tar_loc[1] - pre_loc[1]]
        Data.loc[i, '当前位置']=[now_loc[0]+move_val[0],now_loc[1]+move_val[1]]
        Data.loc[i,'位移量']=move_val
        Data.loc[i, '位移标量'] = sqrt(move_val[0]*move_val[0]+move_val[1]*move_val[1])
    return Data

def solover_loop(Data):
    Mother = Data.loc[Data['状态'] == 'mother']
    Mother = pd.DataFrame(Mother).reset_index()
    Mother = Mother.drop('index', axis=1)
    a = Mother.loc[0, '当前位置']
    b = Mother.loc[1, '当前位置']
    c = Mother.loc[2, '当前位置']
    d = Mother.loc[3, '当前位置']
    noMother = Data.loc[Data['状态'] == 'none']
    noMother = pd.DataFrame(noMother).reset_index()
    noMother = noMother.drop('index', axis=1)
    for i in range(0, len(noMother)):
        v = [noMother.loc[i, '当前位置'][0], noMother.loc[i, '当前位置'][1]]
        val = get_location(a, b, c, d, v,noMother,Mother)
        noMother.loc[i, '预测位置'] = val
    noMother=Moving(noMother)
    val=pd.concat([Mother,noMother]).reset_index()
    val = val.drop('index', axis=1)

    return val