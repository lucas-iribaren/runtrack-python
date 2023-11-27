def distance_to_toilettes(nombre_marches, hauteur_marche):
    distance_totale_par_jour = 5 * (hauteur_marche/100) * 2 * nombre_marches
    distance_totale_par_semaine = distance_totale_par_jour * 7
    print (f"Pour {nombre_marches} marches de {hauteur_marche} cm, le gardien parcourt {distance_totale_par_semaine:.2f} m par semaine.")

distance_to_toilettes(300, 30)