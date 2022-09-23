def plane_add(data, index, code, now_loc, pre_loc, state):
    data.loc[index, '编号'] = code
    data.loc[index, '当前位置'] = now_loc
    data.loc[index, '目标位置'] = pre_loc
    data.loc[index, '预测位置'] = [0, 0]
    data.loc[index, '上次位置'] = [0, 0]
    data.loc[index, '状态'] = state
    data.loc[index, '位移标量'] = 0
    data.loc[index, '位移量'] = [0, 0]
    data.loc[index, '运行步数'] = str(0)
    loc_t = now_loc
    if loc_t[1] == 0:
        loc_t[1] = 1
    data.loc[index, '原点方向量'] = loc_t[0] / loc_t[1]
