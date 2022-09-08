# coding=gbk
import Config

class GSV: #GSV的类创建
    def __init__(self, Position,mission): #GSV的类中 包含有 GSV的位置 GSV任务定时器 GSV任务名称 GSV执行任务所属阶段 GSV目标CNC编号
        self.Position = Position
        self.GSVCounter = 0
        self.MissionName = ''
        self.mission=mission
        self.MissionStage='Stage2'
        self.CNC_Number=''
    def GetWork1(self): #执行单一流程时候的任务获取函数
        val = self.mission.Stack.loc[(self.mission.Stack['任务状态'] == '未完成')]
        stage1=val.loc[(val['任务阶段']=='Stage1')].head(1)
        if (not stage1.empty)and self.MissionStage=="Stage2":
                self.Position =stage1['CNC位置'].values[0]
                self.GSVCounter =stage1['任务所需时间'].values[0]
                self.mission.MissionStart(stage1['任务代号'].values[0])
                self.CNC_Number=stage1['CNC编号'].values[0]
        else:
            self.GSVCounter=0
    def GetWork2(self):#执行双流程时候的任务获取参数
        val = self.mission.Stack.loc[(self.mission.Stack['任务状态'] == '未完成')]
        stage1=val.loc[(val['任务阶段']=='Stage1')].head(1)
        stage2=val.loc[(val['任务阶段']=='Stage2')].head(1)
        if (not stage1.empty)and self.MissionStage=="Stage2":
                self.Position =stage1['CNC位置'].values[0]
                self.GSVCounter =stage1['任务所需时间'].values[0]
                self.mission.MissionStart(stage1['任务代号'].values[0])
                self.CNC_Number = stage1['CNC编号'].values[0]
                self.MissionStage='Stage1'
        else:
            if (not stage2.empty) and self.MissionStage == "Stage1":
                self.Position = stage2['CNC位置'].values[0]
                self.GSVCounter = stage2['任务所需时间'].values[0]
                self.mission.MissionStart(stage2['任务代号'].values[0])
                self.CNC_Number = stage2['CNC编号'].values[0]
                self.MissionStage = 'Stage2'
            else:
                self.GSVCounter=0

    def Loop(self): #GSV的存活函数
        self.GSVCounter -= 1

        if self.GSVCounter <= 0:
            if Config.Two:
                self.GetWork2()
            else:
                self.GetWork1()

