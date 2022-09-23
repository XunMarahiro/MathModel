import pandas as pd
import DataProcess
import DataIn
from Solover import solover_loop
import math
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

now_loc, pre_loc = DataIn.read()
Data = DataProcess.Database(now_loc, pre_loc)
Data.Data.to_excel("开始位置.xlsx", sheet_name='开始位置')
Picture = Data.Data

Times=18
# Data.Data.loc[Data.Data['编号'] == 'E0', '状态'] = 'mother'
# Data.Data.loc[Data.Data['编号'] == 'E1', '状态'] = 'mother'
# Data.Data.loc[Data.Data['编号'] == 'E2', '状态'] = 'mother'
# Data.Data.loc[Data.Data['编号'] == 'E5', '状态'] = 'mother'
#
# Data.Data.loc[Data.Data['状态'] == 'mother', '位移量'] = [[0, 0],[0, 0],[0, 0],[0, 0]]
# Data.Data.loc[Data.Data['状态'] == 'mother', '预测位置'] = [[0, 0],[0, 0],[0, 0],[0, 0]]
# Data.Data = solover_loop(Data.Data)
# Picture = pd.concat([Picture, Data.Data])
#
# Data.Data.loc[:, '状态'] = 'none'
# Data.Data.loc[Data.Data['编号'] == 'E0', '状态'] = 'mother'
# Data.Data.loc[Data.Data['编号'] == 'E1', '状态'] = 'mother'
# Data.Data.loc[Data.Data['编号'] == 'E3', '状态'] = 'mother'
# Data.Data.loc[Data.Data['编号'] == 'E4', '状态'] = 'mother'
# Data.Data.loc[Data.Data['状态'] == 'mother', '位移量'] = [[0, 0],[0, 0],[0, 0],[0, 0]]
# Data.Data.loc[Data.Data['状态'] == 'mother', '预测位置'] = [[0, 0],[0, 0],[0, 0],[0, 0]]
# Data.Data = solover_loop(Data.Data)
# Picture = pd.concat([Picture, Data.Data])
#
# Data.Data.loc[:, '状态'] = 'none'
# Data.Data.loc[Data.Data['编号'] == 'E0', '状态'] = 'mother'
# Data.Data.loc[Data.Data['编号'] == 'E1', '状态'] = 'mother'
# Data.Data.loc[Data.Data['编号'] == 'E3', '状态'] = 'mother'
# Data.Data.loc[Data.Data['编号'] == 'E7', '状态'] = 'mother'
# Data.Data.loc[Data.Data['状态'] == 'mother', '位移量'] = [[0, 0],[0, 0],[0, 0],[0, 0]]
# Data.Data.loc[Data.Data['状态'] == 'mother', '预测位置'] = [[0, 0],[0, 0],[0, 0],[0, 0]]
# Data.Data = solover_loop(Data.    Data)
# Picture = pd.concat([Picture, Data.Data])

for i in range(1, Times):
    Data.Mother_Moving(i,[1,1])
    Data.Get_Mother()
    Data.Data = solover_loop(Data.Data)
    Data.Data.loc[:, '运行步数'] = str(i)
    Picture = pd.concat([Picture, Data.Data])
Picture.to_excel("处理结果.xlsx", sheet_name='最终位置')

plt.figure()
plt.plot(Picture.loc[Data.Data['编号'] == 'E0', '运行步数'], Picture.loc[Data.Data['编号'] == 'E0', '位移标量'],
         label='E0')
plt.plot(Picture.loc[Data.Data['编号'] == 'E1', '运行步数'], Picture.loc[Data.Data['编号'] == 'E1', '位移标量'],
         label='E1')
plt.plot(Picture.loc[Data.Data['编号'] == 'E2', '运行步数'], Picture.loc[Data.Data['编号'] == 'E2', '位移标量'],
         label='E2')
plt.plot(Picture.loc[Data.Data['编号'] == 'E3', '运行步数'], Picture.loc[Data.Data['编号'] == 'E3', '位移标量'],
         label='E3')
plt.plot(Picture.loc[Data.Data['编号'] == 'E4', '运行步数'], Picture.loc[Data.Data['编号'] == 'E4', '位移标量'],
         label='E4')
plt.plot(Picture.loc[Data.Data['编号'] == 'E5', '运行步数'], Picture.loc[Data.Data['编号'] == 'E5', '位移标量'],
         label='E5')
plt.plot(Picture.loc[Data.Data['编号'] == 'E6', '运行步数'], Picture.loc[Data.Data['编号'] == 'E6', '位移标量'],
         label='E6')
plt.plot(Picture.loc[Data.Data['编号'] == 'E7', '运行步数'], Picture.loc[Data.Data['编号'] == 'E7', '位移标量'],
         label='E7')
plt.plot(Picture.loc[Data.Data['编号'] == 'E8', '运行步数'], Picture.loc[Data.Data['编号'] == 'E8', '位移标量'],
         label='E8')
plt.plot(Picture.loc[Data.Data['编号'] == 'E9', '运行步数'], Picture.loc[Data.Data['编号'] == 'E9', '位移标量'],
         label='E9')
plt.legend()  # 添加图例
plt.ylabel('移动距离')
plt.xlabel('处理步数')
plt.title('移动距离随步数的变化')
plt.ylim((0, 15))
plt.savefig('运动量随步数的变化.svg', format='svg', dpi=1600)

plt.figure(figsize=[20,20],dpi=1600)
for step in range(0,Times):
    start=Picture.loc[Picture['运行步数']==str(step),'当前位置']
    print(start)
    for i in range(1,len(start)):
        print([step,i])
        plt.scatter(start[i][0],start[i][1],s=30,c='b',alpha=(step+Times)/2/Times)
plt.title('各无人机位置变化情况',fontsize=50)
plt.savefig('各无人机位置变化情况.svg', format='svg')


for i in range(0, len(Data.Data)):
    for a in ['当前位置', '预测位置', '目标位置', '位移量', '上次位置']:
        x = Data.Data.loc[i, a][0]
        y = Data.Data.loc[i, a][1]
        if x == 0:
            if y > 0:
                Data.Data.loc[i, a] = [y, 90]
            else:
                Data.Data.loc[i, a] = [y, 180]
        else:
            try:
                Data.Data.loc[i, a] = [math.sqrt(math.pow(x, 2) + math.pow(y, 2)), math.tan(y / x)]
            except:
                print(x, y, i, a)

Data.Data.to_excel("结束位置.xlsx", sheet_name='最终位置')
