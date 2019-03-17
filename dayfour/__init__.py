if __name__=='__main__':
    age1=int(input("请输入你的年龄："))
    age2=int(input("请输入他/她的年龄："))
    if age1 > age2:
        print("{0}>{1}".format(age1,age2))
    elif age1<age2:
        print("{0}<{1}".format(age1, age2))
    elif age1==age2:
      print("{0}={1}".format(age1, age2))