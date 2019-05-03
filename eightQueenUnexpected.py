import datetime


def equaltion(x, y, x1, y1):   # 判断k=1的线
    result = (x - x1) - (y - y1)
    return result


def equiltion2(x, y, x1, y1):   # 判断k=-1的线
    result = 0 - (x - x1) - (y - y1)
    return result



start = datetime.datetime.now()

queen = 8
# plate = []  # 第几个元素代表第几行，大小代表第几列
# memory = []  # 记忆列值
# h = 1  # 行
# l = 0  # 列
i = 0   # 答案个数
first = 0   # 第一个皇后的列位置
answer = []   # 储存答案
for first in range(0, queen):
    plate = []   # 每次结束清理棋盘
    memory = []   # 每次结束清理棋盘
    flag = 0   # 冲突标志位
    h = 1   # 从第1行开始判断
    l = 0   # 从第0列开始判断
    plate.append(first)
    memory.append(first)
    while h < queen:  # 放置另外七个皇后
        while l < queen:  # 行不变，挪动列
            if memory.count(l):  # 比较列是否重复
                flag = 1
            if flag != 1:  # 比较斜线是否满足
                for beJudgehH in range(0, len(plate)):   # 从第一个皇后判断到最后一个已经放置的皇后，beJudgehH代表被判断的行
                    if equaltion(plate[beJudgehH], beJudgehH, l, h) == 0:
                        flag = 1
                    if equiltion2(plate[beJudgehH], beJudgehH, l, h) == 0:
                        flag = 1
                    if flag == 1:
                        break
            if flag == 1:  # 以上任意条件满足，则换列判断，直到都不满足
                flag = 0
                l += 1
                continue
            plate.append(l)   # 放置皇后
            memory.append(l)   # 记忆列位置
            l = 0   # 为下一行，列的判断做准备
            break
        if len(plate) != (h + 1):  # 如果没添加上，向后退，将已经放置的皇后列+1，重新进行上述判断
            if len(plate) == 1:   # 如果退到第一个皇后的位置，停止退后
                break
            l = plate[len(plate) - 1] + 1
            h -= 2
            plate.pop()   # 移去上一个已经放置的皇后
            memory.pop()   # 消除上一个的列记录
        if len(plate) == queen:
            i += 1
            print(i, plate, '\n')
            l = plate[len(plate) - 1] + 1
            h -= 2
            plate.pop()
            memory.pop()
        h += 1
end = datetime.datetime.now()   # 计算运算时间
print(end-start)   # 输出时间
