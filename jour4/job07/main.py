def x():
    L = [8, 24,48,2,16]
    y=0
    for i in L:
         if i %3 == 0:
           y+=1 
    print(y)
    print(len([x for x in L if x % 3 == 0]))

x()