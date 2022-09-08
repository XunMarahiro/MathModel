# coding=gbk
import Config
import random

class CNC:
    def __init__(self, CNC_GetTime, CNC_Postion, WorkingTime, CNC_Number, MoveTime, Mission,MissionStage,WashingTime):
        self.CNC_GetTime = CNC_GetTime #CNC上下料时间
        self.CNC_Postion = CNC_Postion #CNC位置
        self.WorkState = 'NoWork'       #CNC工作状态
        self.CNC_Number = CNC_Number    #CNC编号
        self.WorkingTime = WorkingTime #CNC工作时间
        self.WorkingCounter = 0         #CNC任务计时器
        self.WaitingTime = 0            #CNC等待GSV移动过来的时间
        self.Mission = Mission          #读取全部的任务序列
        self.MoveTime = MoveTime        #GSV移动时间的存储数组
        self.MissionStage=MissionStage  #CNC所属的工作流程
        self.WashingTime=WashingTime    #清洗熟件所需时间

    def Require(self, time):            #CNC向任务队列中添加任务需求
        self.Mission.AddMission(time, self.CNC_Number, self.CNC_Postion,self.MissionStage)
        self.WaitingTime = time
        self.WorkState = 'Waiting'

    def Mission_In(self):               #CNC任务被受理的回调函数
        if self.WorkState=="Waiting":
            self.WorkState = 'Working'
            self.WorkingCounter = self.WorkingTime + self.WaitingTime

    def Loop(self, GSV_Position,CNC_Number):    #CNC日常循环 进行基本的任务检索和时间等待
        self.WorkingCounter -= 1
        if (self.WorkingCounter <= 0) and (self.WorkState != 'Waiting'):
            val = self.MoveTime[abs(GSV_Position - self.CNC_Postion)]
            val += self.CNC_GetTime+self.WashingTime
            Trouble=False
            if random.random()<0.01and Config.Random and not Trouble:
                val=val+(random.random()*10+10)*60
                Trouble=True
            self.Require(val)
        if CNC_Number==self.CNC_Number:
            self.Mission_In()
