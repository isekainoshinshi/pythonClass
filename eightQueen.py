def equiltion1(x, y, x1, y1):   # 判断k=1的线
    result = (x - x1) - (y - y1)
    return result


def equiltion2(x, y, x1, y1):   # 判断k=-1的线
    result = 0 - (x - x1) - (y - y1)
    return result


import datetime
start = datetime.datetime.now()

queen = 8
plate = []  # 第几个元素代表第几行，大小代表第几列
memory = []  # 记忆列值
h = 1  # 行
l = 0  # 列
i = 0
answer = []
count = 0   # 计数
# for first in range(0, queen):

plate.append(0)
memory.append(0)
while h < queen:  # 放置另外七个皇后
    while l < queen:  # 行不变，挪动列
        if memory.count(l):  # 比较列是否重复
            flag = 1
        if flag != 1:  # 比较斜线是否满足
            for beJudgehH in range(0, len(plate)):
                if equiltion1(plate[beJudgehH], beJudgehH, l, h) == 0:
                    flag = 1
                if equiltion2(plate[beJudgehH], beJudgehH, l, h) == 0:
                    flag = 1
                if flag == 1:
                    break
        if flag == 1:  # 以上任意条件满足，则换列判断，直到都不满足
            flag = 0
            l += 1
            continue
        plate.append(l)
        memory.append(l)
        l = 0
        break
    if len(plate) != (h + 1):  # 如果没添加上，向后退
        if len(plate) == 0:
            break
        l = plate[len(plate) - 1] + 1
        h -= 2
        plate.pop()
        memory.pop()
    if len(plate) == queen:
        i += 1
        print(i, plate, '\n')
        l = plate[len(plate) - 1] + 1
        h -= 2
        plate.pop()
        memory.pop()
    h += 1
end = datetime.datetime.now()
print (end-start)