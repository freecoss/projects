chaine = input("saisir une chaine de caracteres : ")
count = 0
for i in range(4):
    if chaine[i].isupper():
        count+=1
if count>=2:
    print(chaine.upper())