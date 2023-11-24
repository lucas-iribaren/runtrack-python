L=[71, 19 , 29 ,9 , 1]

def longueur(liste):
    compteur=0
    for i in liste:
        compteur+=1
    return compteur

def tri(liste):
    i = longueur(liste) - 1
    while i > 0:
        j=0
        while j < i:
            if liste[j+1]<liste[j]:
                stock=liste[j+1]
                liste[j+1]=liste[j]
                liste[j]=stock
            j+=1
        i-=1

tri(L)
print(L)