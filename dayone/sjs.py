import  random
if __name__=='__main__':
    ints=input("请输入一个数值：")

    i =random.random()
    if i > float(ints):
        print("{0}>{1}".format(i,float(ints)))
    elif i<float(ints):
        print("{0}<{1}".format(i, float(ints)))
    elif i==float(ints):
        print("{0}={1}".format(i, float(ints)))
