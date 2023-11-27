def arrondir_notes(liste_notes):
    notes_arrondies = []

    for note in liste_notes:
        if note < 40:
            notes_arrondies.append(note)  
        else:
            prochain_multiple_de_5 = (note // 5 + 1) * 5
            difference = prochain_multiple_de_5 - note

            if difference < 3:
                notes_arrondies.append(prochain_multiple_de_5)
            else:
                notes_arrondies.append(note)

    return notes_arrondies

notes = [73, 39, 83, 56, 92]
notes_arrondies = arrondir_notes(notes)
print("Notes d'origine:", notes)
print("Notes arrondies:", notes_arrondies)