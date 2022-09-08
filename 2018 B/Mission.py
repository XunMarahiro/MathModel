# coding=gbk
import pandas as pd

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', 1000)


class Mission:  #���������
    def __init__(self): #��ʼ�� ������ ������� �������ʱ�� ����ʼʱ�� �������ʱ�� ����״̬ ��������ʱ�� CNC��� CNCλ�� ����׶� �Ȳ���
        self.list = {'����': [0], '�������': 'E1', '�������ʱ��': [0], '����ʼʱ��': [0], '�������ʱ��': [0], '����״̬': '', '��������ʱ��': [0],'CNC���': [0],'CNCλ��':[1],'����׶�':'�׶�һ'}
        self.Stack = pd.DataFrame(self.list).set_index('����')
        self.Mission_index = 0
        self.Mission_Time = 0
        self.FinishedMission=pd.DataFrame(self.list).set_index('����')
    def AddMission(self, NeedTime, CNC,CNC_position,MissionStage):  #������������������ĺ��� ��Ҫ���ݵĲ����� ��������ʱ�� CNC��� CNCλ�� �����������̽׶�
        self.Stack.loc[self.Mission_index] = ['E' + str(self.Mission_index), self.Mission_Time, 0, 0, 'δ���', NeedTime,CNC,CNC_position,MissionStage]
        self.Mission_index += 1

    def MissionStart(self, MissionName):    #��ʼ����ĺ��� ���ݲ����� �������
        val=self.Stack.loc[self.Stack['�������'] == MissionName, '��������ʱ��']
        self.Stack.loc[self.Stack['�������'] == MissionName, '����ʼʱ��'] = [self.Mission_Time]
        self.Stack.loc[self.Stack['�������'] == MissionName, '�������ʱ��'] = [self.Mission_Time+val]
        self.Stack.loc[self.Stack['�������'] == MissionName, '����״̬'] = '���'
    def Loop(self,val):        #������еĴ��� ִ��ʱ��ĸ���
        self.Mission_Time=val
