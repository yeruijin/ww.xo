if __name__=='__main__':

    msn=input("enter your self")
    msn=int(msn)
    print("msn")

    if msn <=100 and msn>=0:
        if msn<60:
         print('bad')
        if msn<=80and msn>=60:
            print('good')
        if msn <=100and msn>=80:
            print("excellent")