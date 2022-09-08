# coding=gbk
import Config
import random

class CNC:
    def __init__(self, CNC_GetTime, CNC_Postion, WorkingTime, CNC_Number, MoveTime, Mission,MissionStage,WashingTime):
        self.CNC_GetTime = CNC_GetTime #CNC������ʱ��
        self.CNC_Postion = CNC_Postion #CNCλ��
        self.WorkState = 'NoWork'       #CNC����״̬
        self.CNC_Number = CNC_Number    #CNC���
        self.WorkingTime = WorkingTime #CNC����ʱ��
        self.WorkingCounter = 0         #CNC�����ʱ��
        self.WaitingTime = 0            #CNC�ȴ�GSV�ƶ�������ʱ��
        self.Mission = Mission          #��ȡȫ������������
        self.MoveTime = MoveTime        #GSV�ƶ�ʱ��Ĵ洢����
        self.MissionStage=MissionStage  #CNC�����Ĺ�������
        self.WashingTime=WashingTime    #��ϴ�������ʱ��

    def Require(self, time):            #CNC����������������������
        self.Mission.AddMission(time, self.CNC_Number, self.CNC_Postion,self.MissionStage)
        self.WaitingTime = time
        self.WorkState = 'Waiting'

    def Mission_In(self):               #CNC��������Ļص�����
        if self.WorkState=="Waiting":
            self.WorkState = 'Working'
            self.WorkingCounter = self.WorkingTime + self.WaitingTime

    def Loop(self, GSV_Position,CNC_Number):    #CNC�ճ�ѭ�� ���л��������������ʱ��ȴ�
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
