def longueur(ch):  
    count = 0
    for _ in ch:
        count += 1
    return count

def decouper(chiffre, ch):
    mots = []                     
    debut_mot = 0                
    long_chaine = longueur(ch)   
    nouvelle_chaine = ""         
    i = 0

    while i < long_chaine:                 
        if ch[i] in [" ", ","]:
            mots.append(ch[debut_mot:i])
            debut_mot = i + 1              
        i += 1
    mots.append(ch[debut_mot:])

    for mot in mots:                     
        if longueur(mot) > chiffre:
            nouvelle_chaine += mot + " "
    return nouvelle_chaine.strip()        

phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
resultat = decouper(3, phrase)
print(resultat)
