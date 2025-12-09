mois = (
    ("janvier", 31),
    ("février", 28),
    ("mars", 31),
    ("avril", 30),
    ("mai", 31),
    ("juin", 30),
    ("juillet", 31),
    ("août", 31),
    ("septembre", 30),
    ("octobre", 31),
    ("novembre", 30),
    ("décembre", 31),
)
jour_annee= int(input("entrez un jour entre 1 et 365 : "))
jrs_afficher = jour_annee
for x in mois:
    if jour_annee>x[1]:
        jour_annee-=x[1]
    else:
        print(f"Le jours {jrs_afficher} correspond au {jour_annee} {x[0]}")
        break
    
"""
    `reponse prof`
    i = 0
    while jour_annee>mois[i][i]:
        jour_annee-=mois[i][i]
        i+=1
    print(f"Le jours {jrs_afficher} correspond au {jour_annee} {x[0]}")
"""