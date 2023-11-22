def time_to_text(x):
    y=0
    z=0
    if x % 1 ==0:
        while x >= 60:
            x -= 60
            y+=1
            while y >= 24:
                y -= 24
                z+=1
        print(f"Vos minutes donnent {z}jours {y}heures {x}minutes")

    else:
        print('Veuillez rentrer un nombre entier')

time_to_text(20160)
time_to_text(12)
time_to_text(11111)
