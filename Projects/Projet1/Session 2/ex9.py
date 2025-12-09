flottant = float(input("Saisir un nombre flottant : "))
for i in range(1,int(flottant)):
    if flottant>i**2:
        res = i
    else:
        break
print(res)