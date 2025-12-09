while True:
    note_str = input("Entrez une note entre 0 et 20 : ")
    note = 0
    try:
        note = float(note_str)
    except ValueError:
        print("Note invalide. Veuillez entrer un nombre décimal.")
        continue

    if 0 <= note <= 20:
        break
    print("Note invalide. Veuillez entrer une note entre 0 et 20.")


if 10 <= note < 12:
    print("Mention Passable")
elif 12 <= note < 14:
    print("Mention Assez Bien")
elif 14 <= note < 16:
    print("Mention Bien")
elif 16 <= note <= 20:
    print("Mention Très Bien")
else:
    print("Pas de mention")