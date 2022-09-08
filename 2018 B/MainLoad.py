# -*- coding:utf-8 -*-
import CNC
import Config
import Mission
import GSV
import Time
import pandas as pd

DataBase=Config.DataBase
Two=Config.Two
Random=Config.Random

MoveTime=[[0,20,33,46],[0,23,41,59],[0,18,32,46]]
SingleOneTime=[560,580,545]
DoubleOneTime=[400,280,455]
DoubleTwoTime=[378,500,182]
OneGetTime=[28,30,27]
TwoGetTime=[31,25,32]
WashingTime=[25,30,25]
Stage=[['Stage1','Stage1','Stage1','Stage1','Stage1','Stage1','Stage1','Stage1',],['Stage1','Stage1','Stage1','Stage1','Stage2','Stage2','Stage2','Stage2']]
if not Two:
    DoubleTwoTime=SingleOneTime
    DoubleOneTime=SingleOneTime
if Two:
    Stage=Stage[1]
else:
    Stage=Stage[0]
Current_Time=Time.Time(0)
Loading=Mission.Mission()
CNC1=CNC.CNC(OneGetTime[DataBase],1,DoubleOneTime[DataBase],1,MoveTime[DataBase],Loading,Stage[0],WashingTime[DataBase])
CNC3=CNC.CNC(OneGetTime[DataBase],2,DoubleOneTime[DataBase],3,MoveTime[DataBase],Loading,Stage[1],WashingTime[DataBase])
CNC5=CNC.CNC(OneGetTime[DataBase],3,DoubleOneTime[DataBase],5,MoveTime[DataBase],Loading,Stage[2],WashingTime[DataBase])
CNC7=CNC.CNC(OneGetTime[DataBase],4,DoubleOneTime[DataBase],7,MoveTime[DataBase],Loading,Stage[3],WashingTime[DataBase])
CNC2=CNC.CNC(TwoGetTime[DataBase],1,DoubleTwoTime[DataBase],2,MoveTime[DataBase],Loading,Stage[4],WashingTime[DataBase])
CNC4=CNC.CNC(TwoGetTime[DataBase],2,DoubleTwoTime[DataBase],4,MoveTime[DataBase],Loading,Stage[5],WashingTime[DataBase])
CNC6=CNC.CNC(TwoGetTime[DataBase],3,DoubleTwoTime[DataBase],6,MoveTime[DataBase],Loading,Stage[6],WashingTime[DataBase])
CNC8=CNC.CNC(TwoGetTime[DataBase],4,DoubleTwoTime[DataBase],8,MoveTime[DataBase],Loading,Stage[7],WashingTime[DataBase])

GSV=GSV.GSV(1,Loading)
for i in range(8*60*60):
    Current_Time.Loop()
    CNC1.Loop(GSV.Position,GSV.CNC_Number)
    CNC2.Loop(GSV.Position,GSV.CNC_Number)
    CNC3.Loop(GSV.Position,GSV.CNC_Number)
    CNC4.Loop(GSV.Position,GSV.CNC_Number)
    CNC5.Loop(GSV.Position,GSV.CNC_Number)
    CNC6.Loop(GSV.Position,GSV.CNC_Number)
    CNC7.Loop(GSV.Position,GSV.CNC_Number)
    CNC8.Loop(GSV.Position,GSV.CNC_Number)
    Loading.Loop(Current_Time.RuningTime)
    GSV.Loop()
print(Loading.Stack)

if Two:
    if Random:
        if DataBase==0:
            writer = pd.ExcelWriter('八台机双流程有故障一数据.xlsx')
        if DataBase==1:
            writer = pd.ExcelWriter('八台机双流程有故障二数据.xlsx')
        if DataBase==2:
            writer = pd.ExcelWriter('八台机双流程有故障三数据.xlsx')
    else:
        if DataBase==0:
            writer = pd.ExcelWriter('八台机双流程无故障一数据.xlsx')
        if DataBase==1:
            writer = pd.ExcelWriter('八台机双流程无故障二数据.xlsx')
        if DataBase==2:
            writer = pd.ExcelWriter('八台机双流程无故障三数据.xlsx')
else:
    if Random:
        if DataBase==0:
            writer = pd.ExcelWriter('八台机单流程有故障一数据.xlsx')
        if DataBase==1:
            writer = pd.ExcelWriter('八台机单流程有故障二数据.xlsx')
        if DataBase==2:
            writer = pd.ExcelWriter('八台机单流程有故障三数据.xlsx')
    else:
        if DataBase==0:
            writer = pd.ExcelWriter('八台机单流程无故障一数据.xlsx')
        if DataBase==1:
            writer = pd.ExcelWriter('八台机单流程无故障二数据.xlsx')
        if DataBase==2:
            writer = pd.ExcelWriter('八台机单流程无故障三数据.xlsx')
# Loading.FinishedMission.to_excel(writer,sheet_name='完成任务')
Loading.Stack.to_excel(writer,sheet_name='总任务')

writer.save()
