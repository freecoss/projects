def is_palindrome(mot:str)->bool:
    mot = mot.strip()
    if mot == mot[::-1]:
        return True
    else:
        return False
        
param = str(input("saisir le mot : "))
print(is_palindrome(param))
