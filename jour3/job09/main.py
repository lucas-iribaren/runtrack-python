def moyenne(note1,note2,note3):
    return (note1 + note2 + note3) / 3

print("Veuillez saisir votre première note, nous allons calculer votre moyenne :")
note1= int(input())
print("Veuillez saisir votre deuxième note, nous allons calculer votre moyenne :") 
note2= int(input())
print("Veuillez saisir votre dernière note, nous allons calculer votre moyenne :")
note3= int(input())

moyenne_etudiant=moyenne(note1,note2,note3)

if moyenne_etudiant <= 20 and moyenne_etudiant >= 15:
    print("Très bon élève")
elif moyenne_etudiant <= 14 and moyenne_etudiant >= 11:
    print("Bon élève")
elif moyenne_etudiant <= 10 and moyenne_etudiant >= 8:
    print("Élève moyen")
elif moyenne_etudiant <= 7 and moyenne_etudiant >= 0:
    print("Élève devant faire des efforts")

