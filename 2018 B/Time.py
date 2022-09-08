# coding=gbk
class Time:
    def __init__(self,val):
        self.RuningTime = val
    def TimeAdding(self):
        self.RuningTime+=1
    def Loop(self):
        self.TimeAdding()
        print(self.RuningTime)

