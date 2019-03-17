if __name__=='__main__':
    s = input("请输入任意一个字符串：")

    st=""

    for i in range(0,len(s)):

        if (s.count(s[i])>1):

            if(st.find(s[i])==-1):

                st+=s[i]

    print("原字符串：",s)

    for k in range(0,len(st)):

        print("重复的字符：",st[k],"重复的次数:",st.count(st[k]))
        print("重复过的数组为：",st)








