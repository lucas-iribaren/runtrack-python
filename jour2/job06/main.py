for i in range(1, 1001):
    premier = True

    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            premier = False
            break
    if premier:
        print(i)
    else:
        pass