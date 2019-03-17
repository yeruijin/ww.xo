if __name__=='__main__':
    name='good'
    age=18
    addr='beijing'
    #print的基本使用，不添加任何参数
    print(name,age,addr)
    # print使用，添加sep参数
    #用sep添加分隔符
    print(name, age, addr,sep="-")

    print(name, age, addr,sep="-",end="==")