nombre_marches= int(input('Veuillez rentrer le nombre de marche:'))
hauteur_marche= int(input("Veuillez rentrer la hauteur d'une marche:"))
distance_totale=0

def distance_toilette(nombre_marches, hauteur_marche):
    distance_totale =(nombre_marches * hauteur_marche * 2 * 5 * 7)/100
    return distance_totale 


resultat= distance_toilette(nombre_marches, hauteur_marche)
print (f"Pour {nombre_marches} marches de {hauteur_marche} cm, le gardien parcourt {resultat} m par semaine.")
