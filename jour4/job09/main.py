def x():
    L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
    min=L[0]
    max=L[0]
    for i in L:
        if max < i:
            max=i 
    for i in L:
        if min > i: 
            min=i
    print(f"La valeur min est :{min}")
    print(f"La valeur max est :{max}")
    
x()

        