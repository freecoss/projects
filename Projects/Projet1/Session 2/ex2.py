num1 = int(input("entrer le premier nombre entier"))
num2 = int(input("entrer deuxieme nombre entier"))
op = input("saisir l'operateur")

if op == "+":
    res = num1+num2
elif op == "-":
    res = num1-num2
elif op == "*":
    res = num1*num2
elif op == "/":
    if num2 == 0:
        res = "impossible de diviser par 0"
    else:
        res = num1/num2

print("nombre 1 ",op," nombre 2 =",res)