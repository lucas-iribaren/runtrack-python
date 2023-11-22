def aliment(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "été":
        print("poire, fraise, cassis")
    elif type == "légumes" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "légumes" and saison == "été":
        print("artichaut, aubergine,navet")

aliment("fruits","hiver")
aliment("fruits","été")
aliment("légumes","hiver")
aliment("légumes","été")