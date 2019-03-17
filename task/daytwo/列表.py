if __name__ == '__main__':
    ms=list()
    print(type(ms))
    ms.append("tj")
    print(ms)
    ms.insert(0,"jk")
    print(ms)
    ms.pop()
    print(ms)
    ms.remove()
    print(ms)
    va= ms.pop()
    print("ms.pop = {popva}".format(popva=va))
    del ms
    print(ms)



    del ms
    print(ms)
