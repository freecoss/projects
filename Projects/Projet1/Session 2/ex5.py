import math
poids = float(input("entrez le poids en kg : "))
taille = float(float(input("entrez la taille en cm : "))/100)

imc = float(f'{poids/math.pow(taille,2):.2f}')

print(imc)

if imc>=40:
    inter = "Obésité morbide ou massive"
elif imc>=35 and imc<40:
    inter="Obésité sévère"
elif imc>=30 and imc<25:
    inter="Obésité modérée"
elif imc>25 and imc<35:
    inter = "Surpoids"
elif imc>16.5 and imc<18.5:
    inter = "Maigreur"
elif imc<16.5:
    inter = "Famine"

print("Votre poids en Kg : ",poids,"\n","Votre taille en cm : ",taille*100,"\n","imc : ",imc,"\n","interprétation : ",inter)