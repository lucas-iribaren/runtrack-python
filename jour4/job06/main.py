def x():
    list_nb=[1,2,3,4,5]
    c=list_nb[0]
    list_nb[0]=list_nb[-1]
    list_nb[-1]=c
    print(list_nb)
x()