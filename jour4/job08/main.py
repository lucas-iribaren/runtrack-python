def x():
    L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
    L_fin=0
    for i in L:
        if i % 2 == 0:
            L_fin += i
    print(L_fin)

x()