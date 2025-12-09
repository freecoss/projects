pSeuil = 2.3
vSeuil = 7.41
pression = float(input("enterz la pression : "))
volume = float(input("enterz le volume : "))

if pression>pSeuil and volume>vSeuil:
    print("arrêt immédiat")
if pression>pSeuil:
    print("augmenter le volume de l'enceinte")
if volume>vSeuil:
    print("diminuer le volume de l'enceinte")
else:
    print("tout va bien")
