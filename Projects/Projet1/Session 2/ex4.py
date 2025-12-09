import math
flottant = float(input("Entrez un nombre flottant : "))

if flottant >= 0:
    print(f"{math.sqrt(flottant):.0f}")
else:
    print("impossibe d'avoir un racine d'un nombre negative")