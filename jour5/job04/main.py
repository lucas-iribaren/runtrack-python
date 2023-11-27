def tapis(n):
    print("+"+ "-" * (n+1) + '+' ) 
    for i in range(n+1):
        ligne = ""
        for j in range(n+1):
            if j == n-i:
                ligne += " "
            else:
                ligne += "#"
        print("|"+ligne+"|")
    print("+"+ "-" * (n+1) + '+' ) 

tapis(20)