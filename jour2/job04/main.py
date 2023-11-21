table=int(input())
compteur=0

while compteur< table:
    compteur+=1
    print("Table de multiplication de",compteur)
    for i in range(1, 11):
        result= compteur * i 
        print(compteur,"*",i,"=", result)