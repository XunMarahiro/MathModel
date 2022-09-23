import pandas as pd

square='正方形数据.xlsx'
zhui='锥形数据.xlsx'
round='圆形数据.xlsx'
file=square
def read():
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)
    pointbase=pd.read_excel(file,sheet_name='无人机坐标')
    targetbase=pd.read_excel(file,sheet_name='飞行方阵坐标')
    val1=[]
    val2=[]
    for i in range(len(pointbase)):
        val1.append([pointbase.loc[i,"x"],pointbase.loc[i,"y"]])
        val2.append([targetbase.loc[i,"x"],targetbase.loc[i,"y"]])
    return  val1,val2