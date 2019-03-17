# import random
# if __name__=='__main__':
#     v = random.randint(0,10)
#     print(v)
import random
import time
if __name__ == '__main__':
    v=random.randint(1,10)
    print(v)

    s = random.choice(range(10))
    print(s)
    val = random.randint(1,12)
    print(val)

    print("s={s}".format(s = s))

    mkl="dhniauhfiuahgiuhaugiahfiuahg"
    ss=""
    for i in range(3):
        vs=random.choice(mkl)
        ss+=vs
    print(ss)
    random.seed(10)
    print(random.randint(1,10))
    random.seed(time.time())
    print(random.randint(1,10))

    random.seed(10)

    vss=random.random()
    print(v)

    # random.randrange(stop)
    # random.randrange(start,stop[,step])
    rav = random.randrange(0,10,1)
    print("val={rav}".format(rav=rav))

    mst = ["sda", "dsad", "dasdss"]
    print("before{0}".format(mst))
    random.shuffle(mst)
    print("after{0}".format(mst))
    vb= random.uniform(3,4)
    print(v)
    a1=100
    def ms():
        global a2 #声明a2为全局变量
        a2 = 10
        print("a2={0}".format(a1))
    def mx():
        print("a2={0}".format(a2))

    a1()
    a2()
