# coding=gbk
import pandas as pd

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', 1000)


class Mission:  #任务队列类
    def __init__(self): #初始化 队列有 任务代号 任务进入时间 任务开始时间 任务结束时间 任务状态 任务所需时间 CNC编号 CNC位置 任务阶段 等参数
        self.list = {'索引': [0], '任务代号': 'E1', '任务进入时间': [0], '任务开始时间': [0], '任务结束时间': [0], '任务状态': '', '任务所需时间': [0],'CNC编号': [0],'CNC位置':[1],'任务阶段':'阶段一'}
        self.Stack = pd.DataFrame(self.list).set_index('索引')
        self.Mission_index = 0
        self.Mission_Time = 0
        self.FinishedMission=pd.DataFrame(self.list).set_index('索引')
    def AddMission(self, NeedTime, CNC,CNC_position,MissionStage):  #向任务队列中添加任务的函数 需要传递的参数有 任务所需时间 CNC编号 CNC位置 任务所处流程阶段
        self.Stack.loc[self.Mission_index] = ['E' + str(self.Mission_index), self.Mission_Time, 0, 0, '未完成', NeedTime,CNC,CNC_position,MissionStage]
        self.Mission_index += 1

    def MissionStart(self, MissionName):    #开始任务的函数 传递参数有 任务代号
        val=self.Stack.loc[self.Stack['任务代号'] == MissionName, '任务所需时间']
        self.Stack.loc[self.Stack['任务代号'] == MissionName, '任务开始时间'] = [self.Mission_Time]
        self.Stack.loc[self.Stack['任务代号'] == MissionName, '任务结束时间'] = [self.Mission_Time+val]
        self.Stack.loc[self.Stack['任务代号'] == MissionName, '任务状态'] = '完成'
    def Loop(self,val):        #任务队列的存活函数 执行时间的更新
        self.Mission_Time=val
