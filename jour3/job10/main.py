def pair_impair(nb):
    if nb > 0:
        if nb % 1 == 0:
            if nb % 2:
                print(nb, "est pair")
            else:
                print(nb, "est impair")
        else:
            print("Veuillez rentrez un chiffre entier")
            exit
    else:
        print("Veuillez rentrez un chiffre supérieur à 0")
        exit

pair_impair(-1)
pair_impair(1.5)
pair_impair(2)
pair_impair(3)
pair_impair(-0.3)
