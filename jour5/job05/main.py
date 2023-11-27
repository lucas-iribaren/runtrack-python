def chiffrage(message, decalage):
    resultat = ""
    for lettre in message:
        if lettre.isalpha():
            maj = lettre.isupper()
            indice = ord(lettre.lower()) - ord('a')
            indice_decale = (indice + decalage) % 26
            lettre_decalee = chr(indice_decale + ord('a'))
            if maj:
                lettre_decalee = lettre_decalee.upper()
            resultat += lettre_decalee
        else:
            resultat += lettre

    print(resultat)

chiffrage("Python me casse un peu les pieds",3)
