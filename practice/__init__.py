if __name__ == '__main__':

    strr = input("请任意输出一串字符串")

    strs=""

    for i in range(0,len(strr)):

        if(strr.count(strr[i])>1):

            if(strs.find(strr[i])==-1):

                strs += strr[i]

    print("原字符串：",strr)

    for i in range(0, len(strs)):
        print("重复过的字符为",strs[i],"  出现的次数为：",strr.count(strs[i]))

    print("重复过的字符组成的字符串集合为：",strs)



