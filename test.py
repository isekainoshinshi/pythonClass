#刘敬宇16521125
max = [0,1,2,3,4,5,6,7,8,9]    #循环次数
classInfo = [' ',' ',' ',' ',' ',' ',' ',' '' ',' ']   #设定存放信息大小
endings =  ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']  #日期后缀表
for num in max: #循环10次
    name = input('please input name:')
    stu_num = input('please input number:')
    phone = input('please input phome_num:')
    year = input('please input your birthday year:')
    months = input('please input your birthday months')
    days = input('please input your birthday day:')
    classInfo[num] = [name,stu_num,phone,year,months,days+endings[int(days)-1]]    #依次存储到空间中
print(classInfo)   #显示信息
