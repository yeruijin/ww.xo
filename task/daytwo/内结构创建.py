if __name__ == '__main__':
    mlist = []
    print(type(mlist))
    for l in mlist:
        print("mlist{0}={1}".format(l.__index__(),l))
    for i in mlist:
        print(i)

    mlist[0]=10
    pass
    mlists=[1,2,3,4,5,6]
    print("mlist{0}={1}".format(mlist[2].__index__(),mlist[2]))

    mlistaa=[1,2,3,4,5,6]
    mlistaa1=mlistaa[-2,-4,-1]
    print("id->mlist",id(mlistaa1))
    print("id->mlist", id(mlistaa))
    mk=[1,2,3,4,5,6]
    mj=mk
    print("mk id is (mk)".format(mk=id(mk)))
    print("mk id is (mj)".format(mk=id(mj)))
    print(id(mk))
    del mk[0]
    print(mk)
    print(id(mk))

    mjsss=[1,2,3,4,5,6,7,8,9]
    t=2
    print("in->",t in mjsss)
    print("in->", t not in mjsss)

