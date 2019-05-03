sentence = "welcome my friend!"
screen_width = 80
welcome = ['w', 'e', 'l', 'c', 'o', 'm', 'e']
text_width = len(sentence)
oneSecond = text_width//2
database = [['admin', 'admin']]
privateInfo = [['0', '0', '0']]


# 主函数
def main():
    # 欢迎界面  完成
    i = 0
    for number in range(0, oneSecond):
        if (i == 0) or (i == oneSecond - 1):
            print(' ' * (((screen_width - oneSecond) // 2) - 1 - i) + '/' + '-' * (oneSecond - 1 + 2 * i) + '\\')
        else:
            print(' ' * (((screen_width - oneSecond) // 2) - 1 - i) + '/' + welcome[i - 1] + ' ' * (
                        oneSecond - 3 + 2 * i) + welcome[i - 1] + '\\')
        i += 1
    # 主界面   完成
    while 1:
        choose0 = int(input('1.登录\n' + '2.注册\n'))
        # 登陆账号  完成
        if choose0 == 1:
            info = getInfo()
            if info in database:
                flag = database.index(info)
            else:
                flag = -1
                print("账号或密码错误，请重新尝试")
        # 注册账号  完成
        if choose0 == 2:
            info = getInfo()
            database.append(info)
            privateInfo.append([' ', ' ', ' '])
            flag = -1
            print('注册成功')
        # 登录成功，账号管理系统   完成
        while flag != -1:
            # 管理员用户
            if flag == 0:
                while 1:
                    choose1 = int(input("1.删除用户\n" + "2.显示所有信息\n" + "3.注销\n"))
                    if choose1 == 1:
                        flag = int(input())
                        del database[flag]
                        del privateInfo[flag]
                    if choose1 == 2:
                        print(database)
                        print(privateInfo)
                    if choose1 == 3:
                        break
                break
            choose1 = int(input("1.填写个人信息\n" + "2.修改个人信息\n" + "3.修改登陆密码\n" + "4.注销\n"))
            # 填写个人信息    完成
            if choose1 == 1:
                while 1:
                    choose2 = int(input('1.姓名\n' + '2.性别\n' + '3.电话\n' + '4.返回\n'))
                    if choose2 == 1:
                        if privateInfo[flag][0] == ' ':
                            privateInfo[flag][0] = input('请输入姓名：')
                        else:
                            print("已有信息，无法添加")
                    if choose2 == 2:
                        if privateInfo[flag][1] == ' ':
                            privateInfo[flag][1] = input('请输入性别：')
                        else:
                            print("已有信息，无法添加")
                    if choose2 == 3:
                        if privateInfo[flag][2] == ' ':
                            privateInfo[flag][2] = input('请输入电话：')
                        else:
                            print("已有信息，无法添加")
                    if choose2 == 4:
                        break
            # 修改个人信息    完成
            if choose1 == 2:
                while 1:
                    choose3 = int(input('1.姓名\n' + '2.性别\n' + '3.电话\n' + "4.返回\n"))
                    if choose3 == 1:
                        privateInfo[flag][0] = input('请输入姓名：')
                    if choose3 == 2:
                        privateInfo[flag][1] = input('请输入性别：')
                    if choose3 == 3:
                        privateInfo[flag][2] = input('请输入电话：')
                    if choose2 == 4:
                        break
            # 修改密码  完成
            if choose1 == 3:
                originalPasswords = input('请输入原先的密码')
                if originalPasswords == database[flag][1]:
                    database[flag][1] = input('请输入新密码')
                    print('修改成功')
            # 注销    完成
            if choose1 == 4:
                flag = -1
            if (not ((choose1 >= 1) and (choose1 <= 4))):
                print('请输入一个有效的选项')


# 账号密码读取    完成
def getInfo():
    account = input("请输入您的账号:")
    passwords = input("请输入您的密码:")
    info = [account, passwords]
    return info


# 调用主函数
main()