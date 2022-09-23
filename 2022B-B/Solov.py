import math
from math import sqrt, pow, acos, pi, fabs
import pandas as pd

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


def FindAngle(a, c, v):
    A = angel(a, c, v)
    return A


def solover(c1, c2, c3,c4, v, a, b,c,d):
    if v == a or v == b or v == c or v == d:
        return 10
    else:
        A = angel(a, b, v)
        B = angel(b, c, v)
        C = angel(c, d, v)
        D = angel(d, a, v)
        return fabs(A - c1) + fabs(B - c2) + fabs(C - c3)+ fabs(D - c4)


def Moving(Data):
    for i in range(0, len(Data)):
        now_loc = Data.loc[i, '当前位置']
        Data.loc[i, '上次位置'] = now_loc
        pre_loc = Data.loc[i, '预测位置']
        tar_loc = Data.loc[i, '目标位置']
        move_val = [tar_loc[0] - pre_loc[0], tar_loc[1] - pre_loc[1]]
        Data.loc[i, '当前位置'] = [now_loc[0] + move_val[0], now_loc[1] + move_val[1]]
        Data.loc[i, '位移量'] = move_val
        Data.loc[i, '位移标量'] = sqrt(move_val[0] * move_val[0] + move_val[1] * move_val[1])
    return Data
def caul_distance(a,b):
    return math.sqrt(math.pow(a[0]-b[0],2)+math.pow(a[1]-b[1],2))

def solov(a, b,c,d, c1, c2, c3,c4, now_tar, pre,v):
    Step = 2
    S=100
    val_smal = 20
    final = pre
    base=now_tar
    Flag=0
    Loopcounter=0
    goaway=1
    while val_smal>goaway:
        go = int(S / Step)
        x = base[0]-S
        for m in range(0,2*go):
            y=base[1]-S
            for n in range(0,2*go):
                val = solover(c1, c2, c3,c4, [x, y], a, b,c,d)
                if Step <= 0.05:
                    Step = 0.5
                if val_smal > val  and Flag !=1:
                    val_smal = val
                    final = [x,y]
                    if Step <= 0.01:
                        Step = 0.1
                    if caul_distance([x,y],now_tar)<20:
                        Loopcounter=0
                        Flag=1
                        base = [x, y]
                y=y+Step
            x=x+Step
        Loopcounter+=1
        if Loopcounter>1:
            goaway+=0.1
            Loopcounter=0
            Flag=1

        if Flag :
            Step = Step -0.01
            S = S -1
            Flag=0
            if S<20:
                S=20
            print(base,v,now_tar,S,Step,val_smal)
    return final


def solov_loop(Data):
    Mother = Data.loc[Data['状态'] == 'mother']
    Mother = pd.DataFrame(Mother).reset_index()
    Mother = Mother.drop('index', axis=1)
    a = Mother.loc[1, '当前位置']
    b = Mother.loc[2, '当前位置']
    c = Mother.loc[3, '当前位置']
    d= [0,0]
    noMother = Data.loc[Data['状态'] == 'none']
    noMother = pd.DataFrame(noMother).reset_index()
    noMother = noMother.drop('index', axis=1)
    for i in range(0, len(noMother)):
        pre = noMother.loc[i, '预测位置']
        v = [noMother.loc[i, '当前位置'][0], noMother.loc[i, '当前位置'][1]]
        t = [noMother.loc[i, '目标位置'][0], noMother.loc[i, '目标位置'][1]]
        c1 = angel(a, b, v)
        c2 = angel(b, c, v)
        c3 = angel(c, d, v)
        c4 = angel(d, a, v)
        val = solov(Mother.loc[1, '目标位置'], Mother.loc[2, '目标位置'],Mother.loc[3, '目标位置'],[0,0], c1, c2, c3,c4, t, pre,v)
        print(val)
        noMother.loc[i, '预测位置'] = val
    noMother = Moving(noMother)
    val = pd.concat([Mother, noMother]).reset_index()
    val = val.drop('index', axis=1)
    return val
