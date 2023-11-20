montant_initial=50000
taux_rendement=0.08
gain_annuel_initial = montant_initial * taux_rendement
print("Gain annuel initial :", gain_annuel_initial,"€")


montant_initial+=5000
taux_rendement+=0.02
gain_annuel_initial = montant_initial * taux_rendement
print("Gain annuel initial :", gain_annuel_initial,"€")


montant_initial-=0.1
taux_rendement-=0.01
gain_annuel_initial = montant_initial * taux_rendement
print("Gain annuel initial :", gain_annuel_initial,"€")