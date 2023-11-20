print("Veuillez insérer votre phrase:")
chaine=input()

nombre_e= chaine.count("e")
if nombre_e > 0 :
    print("Votre phrase contient", nombre_e, "fois la lettre 'e'.")
else :
    print("Votre phrase ne contient pas de 'e' ")




print("Veuillez insérer votre phrase:")
chaine=input()
nombre_e = 0 
for i in chaine:
    if i == 'e':
       nombre_e += 1

print("Votre phrase contient", nombre_e, "fois la lettre 'e'.")
