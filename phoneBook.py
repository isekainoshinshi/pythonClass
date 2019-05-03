# 通信录登录界面
print('⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⠠⠠⠒⠒⠄⠉⠈⠉⠉⠁⠙⠐⠒⠒⠄⢄⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n\
⠄⠄⠄⠄⠄⢀⣠⣤⣴⣶⣤⣤⡠⡰⠊⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠱⢦⢄⣠⣤⣶⣦⣤⣄⡀⠄⠄⠄⠄⠄\n\
⠄⠄⠄⢀⣴⠟⠋⠉⠉⣉⡍⠙⠻⢧⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⡼⠟⠋⠩⣉⠉⠉⠙⠻⣦⡀⠄⠄⠄\n\
⠄⠄⠄⡞⠁⠄⠄⡠⠜⠁⠄⠄⠄⠄⠱⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⠎⠄⠄⠄⠄⠈⠣⢄⠄⠄⠈⢳⠄⠄⠄\n\
⠄⠄⠄⠄⠄⢠⡞⠁⠄⠄⠄⠄⠄⠄⠄⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠄⠄⠄⠄⠄⠄⠄⠈⠳⡄⠄⠄⠄⠄⠄\n\
⠄⠄⠄⠄⣴⣫⣤⣐⠒⠒⠂⠄⠄⠒⠒⠂⠤⢀⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣠⣤⣐⠒⠒⠄⠄⠐⠒⠒⠂⠤⢙⣦⠄⠄⠄⠄\n\
⠄⠄⡠⢪⣿⣿⣿⣿⣧⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠑⢄⠄⠄⠄⠄⠄⠄⠄⠄⡠⢪⣿⣿⣿⣿⣧⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠑⢄⠄⠄\n\
⠄⢰⠄⠈⢿⣿⣿⣿⡏⠠⠤⠤⠤⠤⠄⣀⡀⠄⠄⠄⠄⠃⠄⠄⠄⠄⠄⠄⠘⠄⠈⢿⣿⣿⣿⡏⠠⠤⠤⠤⠤⠄⣀⡀⠄⠄⠄⠄⡆⠄\n\
⠄⣸⡖⠒⠈⠉⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠁⠐⠂⠁⠄⠄⠄⠄⠄⠄⠈⠐⠂⠈⠉⠉⠄⠄⠄⠄⠄⠄⠄⠄⡀⠄⠉⠁⠐⣶⣇⠄\n\
⢠⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣤⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄\n\
⣸⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇\n\
⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿\n\
⣿⣿⠄⠄⢀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡀⠄⠄⣿⣿\n\
⣿⣿⠄⠄⠸⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠇⠄⢰⣿⣿\n\
⢹⣿⣇⠄⠄⣇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣸⠄⠄⣸⣿⡏\n\
⠘⣿⣿⡄⠄⠸⡄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢠⠇⠄⣰⣿⣿⠃\n\
⠄⢹⣿⣿⡄⠄⢹⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⡏⠄⢠⣿⣿⡏⠄\n\
⠄⠄⢿⣿⣿⣄⠄⠹⣦⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣴⠏⠄⣰⣿⣿⡿⠄⠄\n\
⠄⠄⠈⢿⣿⣿⣧⡀⠘⢿⣄⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣠⡿⠃⣀⣶⣿⣿⡿⠁⠄⠄\n\
⠄⠄⠄⠄⠻⣿⣿⣿⣦⡀⡙⢷⣦⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⣴⡾⢋⢠⣼⣿⣿⣿⠟⠄⠄⠄⠄\n\
⠄⠄⠄⠄⠄⠘⢿⣿⣿⣿⣶⣄⠉⠻⢷⣦⣄⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣠⣴⡾⠟⠉⣠⣶⣿⣿⣿⡿⠃⠄⠄⠄⠄⠄\n\
⠄⠄⠄⠄⠄⠄⠄⠙⢿⣿⣿⣿⣿⣶⣄⠉⠛⠿⢿⣶⣶⣤⣤⣤⣤⣤⣤⣤⣤⣶⣾⡿⠿⠛⠉⣠⣴⣾⣿⣿⣿⡿⠋⠄⠄⠄⠄⠄⠄⠄\n\
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣿⣿⣿⣿⣶⣤⣄⣈⣉⣉⠉⠉⠉⠉⣉⣉⣁⣤⣴⣶⣿⣿⣿⣿⣿⣿⠟⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄\n\
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n\
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠙⠛⠿⠿⢿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠛⠋⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄')
print('⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄欢迎来到通讯录系统⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄')
database = {}
# 操作界面
while 1:
    while 1:
        print('请选择操作')
        print('1.添加联系人')
        print('2.删除联系人')
        print('3.修改联系人信息')
        print('4.列出所有联系人')
        select = int(input())
        # 添加新成员
        if select == 1:
            name = input('please input your name')
            sex = input('please input your sex')
            age = input('please input your age')
            address = input('please input your adress')
            person = {name: {'name': name, 'sex': sex, 'age': age, 'address': address}}
            database.update(person)
        # 删除联系人
        if select == 2:
            name = input('please input name which you wanna delate')
            database.pop(name)
        # 更改信息
        if select == 3:
            while 1:
                name = input('change who? input "quit" to quit')
                if database.get(name) == None:
                    print('no this people')
                if name == quit:
                    break
            if name == quit:
                continue
            # 选择更改哪一个信息
            while 1:
                select = int(input('whitch one you wanna change?\n'
                                   '1.name\n'
                                   '2.sex\n'
                                   '3.age\n'
                                   '4.address\n'
                                    '5.exit\n'))
                # 更改名字，更改所有含姓名的地方
                # 添加新名字的成员，删除旧名字的成员
                # 其他数据通过查字典更改
                if select == 1:
                    select = 'name'
                    newname = input('please input your new name')
                    database.get(name)[select] = newname
                    database.update({newname: database.get(name)})
                    del database[name]
                    name = newname
                    continue
                if select == 2:
                    select = 'sex'
                if select == 3:
                    select = 'age'
                if select == 4:
                    select = 'address'
                if select == 5:
                    break
                newinfo = input('please input {}'.format(select))
                database.get(name)[select] = newinfo
                database.update()
        # 显示通信录
        if select == 4:
            print('{}'.format(database.items()))