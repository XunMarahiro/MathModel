# coding=gbk
import Config

class GSV: #GSV���ഴ��
    def __init__(self, Position,mission): #GSV������ ������ GSV��λ�� GSV����ʱ�� GSV�������� GSVִ�����������׶� GSVĿ��CNC���
        self.Position = Position
        self.GSVCounter = 0
        self.MissionName = ''
        self.mission=mission
        self.MissionStage='Stage2'
        self.CNC_Number=''
    def GetWork1(self): #ִ�е�һ����ʱ��������ȡ����
        val = self.mission.Stack.loc[(self.mission.Stack['����״̬'] == 'δ���')]
        stage1=val.loc[(val['����׶�']=='Stage1')].head(1)
        if (not stage1.empty)and self.MissionStage=="Stage2":
                self.Position =stage1['CNCλ��'].values[0]
                self.GSVCounter =stage1['��������ʱ��'].values[0]
                self.mission.MissionStart(stage1['�������'].values[0])
                self.CNC_Number=stage1['CNC���'].values[0]
        else:
            self.GSVCounter=0
    def GetWork2(self):#ִ��˫����ʱ��������ȡ����
        val = self.mission.Stack.loc[(self.mission.Stack['����״̬'] == 'δ���')]
        stage1=val.loc[(val['����׶�']=='Stage1')].head(1)
        stage2=val.loc[(val['����׶�']=='Stage2')].head(1)
        if (not stage1.empty)and self.MissionStage=="Stage2":
                self.Position =stage1['CNCλ��'].values[0]
                self.GSVCounter =stage1['��������ʱ��'].values[0]
                self.mission.MissionStart(stage1['�������'].values[0])
                self.CNC_Number = stage1['CNC���'].values[0]
                self.MissionStage='Stage1'
        else:
            if (not stage2.empty) and self.MissionStage == "Stage1":
                self.Position = stage2['CNCλ��'].values[0]
                self.GSVCounter = stage2['��������ʱ��'].values[0]
                self.mission.MissionStart(stage2['�������'].values[0])
                self.CNC_Number = stage2['CNC���'].values[0]
                self.MissionStage = 'Stage2'
            else:
                self.GSVCounter=0

    def Loop(self): #GSV�Ĵ���
        self.GSVCounter -= 1

        if self.GSVCounter <= 0:
            if Config.Two:
                self.GetWork2()
            else:
                self.GetWork1()

