import random
if __name__ == '__main__':
    mu= [3,7,4,2]
    random.shuffle(mu)
    print(mu)
    mu.sort(reverse=True)
    print(mu)
    mu.sorted(reverse=True)
    print(mu)
    mu.reverse()
    print(mu)
    print(mu.__len__())
    mus=len(mu)
    print(mus)