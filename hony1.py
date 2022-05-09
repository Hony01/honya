# temp=float(input('请输入当天温度：'))   #得到一个字符串,强制装换成浮点数
# if temp >=29:   #条件语句
#     print('今天温度高！')   #缩进四个空格，不可以随便更改
#     print('建议开空调!')
# num=int(input('请输入一个数字:'))
# if num%2 ==0:
#     print('这个数偶数！')
# print('程序结束!')


# string="Python"
# abc=input('请输入一个字母:')
# if abc in string:
#     print('这个字母在string里!')
# print('程序结束!')


# danci=input('请输入一个单词:')
# if len(danci) >6:
#     print('单词太长，记不住!')
# else :
#     print('可以记住!')


# print('请输入一组数字:')
# a=int(input())
# b=int(input())
# c=int(input())
# if a>b:



# score=float(input('请输入你的成绩:'))
# if score >=60:
#     print('及格了！')
# else :
#     print('成绩不及格！')


# import random
# num1=random.randint(1,10)  #产生一个随机数
# print(num1)    #打印随机数
# num2=int(input('请输入1-10的数字:'))
# if num1==num2:
#     print('恭喜你赢了!')
# else :
#     print('小辣鸡!')


#
# print('登录系统')
# root=input('请输入用户名:')
# password=(input('请输入用户密码:'))
# if root=='Tom' and password=='123':
#     print('登陆成功!')
# else :
#     print('登陆失败!')


# age=float(input('请输入您的年龄:'))
# if age>=18:
#     print('您已成年!')
# else :
#     print('你未成年！')


# score=float(input('请输入您的成绩:'))
# if score >90:
#     print('优秀!')
# elif score >80:
#     print('良好!')
# elif score >70:
#     print('中等!')
# elif score >60:
#     print('及格!')
# else :
#     print('不及格!')

# jj=float(input('请输入你的血液中酒精含量:'))
# if jj <=20:
#     print('您未酒驾驾驶!')
# elif jj <80:
#     print('您酒驾驾驶!')
#     print('扣12分，并处暂扣驾照6个月，罚款1000元至2000元')
# else :
#     print('驾驶机动车辆拟将一律吊销驾照，并在5年之内不得重新取得，按照“危险驾驶”定罪，处以拘役。')

# print('门票售票处:')
# age=float(input('请输入您的年龄:'))
# if 1<=age<=14:
#     print('免票')
# elif 15<=age<=64:
#     print('350元')
# else:
#     print('200')


# sex=input('请输入性别：boy/girl:')
# if sex=='boy':
#     weight=float(input('请输入您的体重:'))
#     age=int(input('请输入您的年龄:'))
#     if weight>=50 and 18<=age<=60:
#         print('符合献血条件!')
#     else :
#         print('不符合献血条件!')
# elif sex=='girl':
#     weight=float(input('请输入您的体重:'))
#     age=int(input('请输入您的年龄:'))
#     if weight>=45 and 18<=age<=55:
#         print('符合献血条件!')
#     else :
#         print('不符合献血条件!')
# else:
#     print('输入错误!')


# print('门票售票处:')
# age = float(input('请输入您的年龄:'))
# if  age<=14:
#     print('免票')
# elif age < 65:
#     job = input('请输入您的职业:')
#     if job == '医生' or job == '护士':
#         print('您幸苦了！本景点对您免票!')
#     else:
#      print('350元')
# else:
#     print('200')


# # a=1
# # while a<=10:
# #     print(a)
# #     a=a+1    #a增加1
# print()


#
# a=int(print("请输入一个数字："))














#
# list1=[10,12,7,6,5,22,19]
# for elem in list1:        #从list中逐个取出它的元素，赋值给elem，执行下面的代码快
#     if elem % 2 !=0:     #取余，不等于零，说明是奇数
#         continue         #结束本轮循环，进行下一轮
#     print(elem)







# list1=[10,12,7,6,5,22,19]
# for elem in list1:        #从list中逐个取出它的元素，赋值给elem，执行下面的代码快
#     if elem % 2 !=0:     #取余，不等于零，说明是奇数
#         break       #结束本轮循环
#     print(elem)
#







#
# string="hello,python!"
# for char in string :
#     if char=="o":
#         continue
#     elif char=="n":
#         break
#     else:
#         print(char)





# for a in range(1,10):
#     for b in range(1,a+1):
#         print(a,"*",b,"=",a*b,end="  ")
#     print("")





# a=["大白菜","土豆","萝卜","四季豆","西红柿"]
# b=["猪肉","牛肉","鸡肉"]
#
# for veg in a:
#     for meat in b:
#         print(meat,"炒",veg)




# list=[26,12,38,6,23,3,19,34,25,7,14]
# max=0
# min=0
# for a in list:
#     for b in list:
#         if a>ma
#
#
# print("max",max)
# print("min",min)



# user_name=[]
# user_password=[]
#
# user=[]
#
# flag = True
# while flag:
#     print('-'*20)
#     print('1.注册账号')
#     print('2.登录账号')
#     print('3.退出')
#     i=int(input('请您选择相应的功能：'))
#     print('-'*20)
#     if i == 1:
#         print('---注册账号---')
#         name=input('请输入您的账号：')
#         password=input('请输入您的密码：')
#         user_name.append(name)
#         user_password.append(password)
#         user = list(zip(user_name, user_password))
#     if i == 2:
#         n = 1
#         while n<=5:
#             if n!=5:
#                 print(f'第{n}次机会')
#             else:
#                 print('这是最后一次机会啦！')
#             name = input('请输入您的账号：')
#             password = input('请输入您的密码：')
#             for x in user:
#                 if name == x[0]:
#                     if password == x[1]:
#                         print('登录成功！')
#                         print('欢迎进入系统！')
#                         flag = False
#                         n = 5
#                         break
#                     else:
#                         print('密码错误！')
#                 elif x == user[len(user)-1]:
#                     print('账号或密码错误！')
#                     if n == 5:
#                         print('您错误次数已太多，请稍后再试！')
#                         flag = False
#             n=n+1
#
#     if i == 3:
#         break



#
# pets={'旺财':15,'小黑':12,'大黄':14}
# a=pets['大黄']
# print(f'大黄的体重为{a}')
# pets['樱桃']=26
# for (b,c) in pets.items():
#     c=c+1
#     print(f'{b}过年后的体重为{c}')
# pets.pop('樱桃')
# print(f'还剩{pets}')




# films={'你好，李焕英':49.2,'人潮涌动':5.01,'刺杀小说家':9.22,'熊出没':5.69,'新封神':4.06,'猫和老鼠':0.86,'唐人街探案 3':43.6}
# films['待神令']=2.61
# films.pop('猫和老鼠')
# print(films)
# a=films['刺杀小说家']
# print(f'’刺杀小说家‘的票房收入为{a}')
# b=0
# total=0
# for (k,i) in films.items():
#     if i>b:
#         b=i
#         print(f'电影票房最高的是{k}')
#     total=total+i
# print(f'所有票房总收入为{total}')
# avg=total/len(films.values())
# print(f'每部电影的平均收入为{avg}')


# Users={}
# def addStudent():
#     name=input("请输入学生姓名:")
#     sex=input("请输入性别:")
#     phoneNum=input("请输入电话号码:")
#     pro=input("请输入所修专业:")
#     Users.update({phoneNum:[("性别",sex),("姓名",name),("专业",pro),('角色',"学生")]})
#
# def addTeacher():
#     name = input("请输入教师姓名:")
#     sex = input("请输入性别:")
#     phoneNum = input("请输入电话号码:")
#     office = input("请输入办公室:")
#     Users.update({phoneNum: [("性别", sex), ("姓名", name), ("办公室", office), ('角色', "教师")]})
#
#
#
# def showAllUser():
#     for i,k in Users.items():
#         print(f"{k[3][1]}姓名: {k[1][1]},性别:{k[0][1]},电话号码:{i},{k[2][0]}:{k[2][1]}")
#
#
# def searchUser():
#     phoneNum=input("请输入电话号码:")
#     for i,k in Users.items():
#         if i==phoneNum:
#             print(f"{k[3][1]}姓名: {k[1][1]},性别:{k[0][1]},电话号码:{i},{k[2][0]}:{k[2][1]}")
#
#
# def menu():
#     wellcome = '''
# ***************************
# 欢迎使用=通讯录管理系统= v1.0
# 1.添加学生
# 2.添加教师
# 3.显示所有联系人
# 4.查询联系人
# 0.退出系统
# ***************************
# '''
#     while True:
#         print(wellcome)
#         choose=input("请选择所需的功能:")
#         if choose=='1':
#             addStudent()
#         elif choose=='2':
#             addTeacher()
#         elif choose=='3':
#             showAllUser()
#         elif choose=='4':
#             searchUser()
#         elif choose=='0':
#             print('再见')
#             exit()
#
# if __name__ == '__main__':
#     menu()



def alcohol(a):
