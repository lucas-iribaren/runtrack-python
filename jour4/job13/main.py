L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

def remove_duplicates(L):
    liste_unique = []
    deja_vu = {}
    for num in L:
        if num not in deja_vu:
            liste_unique.append(num)
            deja_vu[num] = True
    return liste_unique

result = remove_duplicates(L)
print(result)
