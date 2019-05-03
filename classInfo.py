database = {'admin': {'password': 'admin'}}
infoDatabase = {}
wordList = {1: {'username': '账号', 'password': '密码'},
            2: {'name': '姓名', 'sex': '性别', 'class': '班级', 'phoneNum': '电话', 'academy': '学院', 'point': '加权分'}}


def getInfo(i, flag):
    int(i)
    flag = '{' + flag + '}'
    info = input('请输入{}'.format(flag).format_map(wordList[i]))
    if flag == 'point':
        info = float(info)
    return info


def updateInfo(username, info, flag):
    info = {flag: info}
    infoDatabase[username].update(info)


def interface(flag):
    if flag == 'student':
        print('1.更改信息')
        print('2.列出加权分')
        print('3.注销')
    if flag == 'admin':
        print('1.更改学生登录信息')
        print('2.增加学生')
        print('3.注销')
    if flag == 'stuInfo':
        print('1.姓名')
        print('2.性别')
        print('3.所在班级')
        print('4.电话')
        print('5.所在学院')
        print('6.加权分')
        print('7.密码')
        print('8.返回')
    return int(input())


def switch():
    username = getInfo(1, 'username')
    password = getInfo(1, 'password')
    if database.get(username):
        if database[username]['password'] == password:
            if username == 'admin':
                logIn = 'admin'
            else:
                logIn = 'student'
    else:
        print('账号或者密码错误')
        return 0
    return logIn, username


def main():
    while 1:
        choose, username = switch()
        if choose == 0:
            continue
        if choose == 'admin':
            while 1:
                num = interface('admin')
                if num == 1:
                    username = getInfo(1, 'username')
                    if database.get(username):
                        database[username]['password'] = '000000'
                        print('重置成功')
                    else:
                        print('没有此人')
                if num == 2:
                    username = getInfo(1, 'username')
                    if not database.get(username):
                        initiate = {username: {'password': '000000'}}
                        initiateInfo = {
                            username: {'name': '', 'sex': '', 'class': '', 'phoneNum': '', 'academy': '', 'point': ''}}
                        database.update(initiate)
                        infoDatabase.update(initiateInfo)
                if num == 3:
                    break
        if choose == 'student':
            while 1:
                num = interface('student')
                if num == 1:
                    while 1:
                        num = interface('stuInfo')
                        if num == 1:
                            flag = 'name'
                        if num == 2:
                            flag = 'sex'
                        if num == 3:
                            flag = 'class'
                        if num == 4:
                            flag = 'phoneNum'
                        if num == 5:
                            flag = 'academy'
                        if num == 6:
                            flag = 'point'
                        if num == 7:
                            password = getInfo(1, 'password')
                            database[username]['password'] = password
                            continue
                        if num == 8:
                            break
                        updateInfo(username, getInfo(2, flag), flag)
                if num == 2:
                    temp = list(infoDatabase.values())
                    pointList = []
                    for i in range(len(infoDatabase)):
                        pointList.append((temp[i]['point'], temp[i]['name']))
                        print(sorted(pointList))
                if num == 3:
                    break


main()
