def x():
    L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
    j=1
    for i in L:
        if i in range(25,90):
            j*=i
    print(j)

x()