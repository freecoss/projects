vehicules = ["train","bus","voiture","velo"]
couleurs = ["rouge","vert","blue","jaune"]

vehicules_couleurs = []

for x in vehicules:
    for y in couleurs:
        if y =="vert" and x == "voiture":
            continue
        a= f"{x} {y}"
        vehicules_couleurs.append(a)

for x in vehicules_couleurs:
    print(x,end=" ~ ")