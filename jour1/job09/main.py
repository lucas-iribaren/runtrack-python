nom="Alpine A110"
prix_unitaire=62500
quantité_en_stock=115

print("Veuillez rentrez la quantité d'", nom, 'souhaité :')
quantité_choisi=(int(input()))

print("Client - Le prix d'une", nom , 'est de', prix_unitaire,'€ \n Vous vous apprêter à acheter',quantité_choisi,nom,"Soit:",(quantité_choisi * prix_unitaire),"€")


prix_unitaire += prix_unitaire * (10 / 100)

print("Malheureusement avec l'inflation le prix actuel est d'une",nom,"est de :", prix_unitaire, "€\n Soit (",prix_unitaire,"*",quantité_choisi,") =",(prix_unitaire * quantité_choisi),"€")



print("\nEntreprise - Il reste actuellement", (quantité_en_stock - quantité_choisi), nom, "en stock")