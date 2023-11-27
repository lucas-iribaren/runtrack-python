def arrondir(num):
    entier = num // 1
    decimal = num % 1
    if decimal >= 0.5:
        entier += 1
    return int(entier) 

def longueur(lst):
    count = 0
    for _ in lst:
        count += 1
    return count

def tri_bulle(lst):
    n = longueur(lst) - 1
    while n > 0:
        j = 0
        while j < n:
            if lst[j + 1] < lst[j]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]
            j += 1
        n -= 1

L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

L_arrondie = []
for i in L:
    L_arrondie += [arrondir(i)]

tri_bulle(L_arrondie)

L_arrondie_entier = [int(x) for x in L_arrondie]
print(L_arrondie_entier)
