days = int(input("saisir le nombre des jours : "))
annee = int(days / 365)
jours_restant  = days%365
semaine =int(jours_restant / 7)
jours =  int(jours_restant%7)

print(days," Jours = ",annee," annee(s) ",semaine," semaine(s) ",jours," Jour(s)")