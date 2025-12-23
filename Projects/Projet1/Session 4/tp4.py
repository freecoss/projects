dictionnaire_pays_capitales = { 
'France': 'Paris', 
'Allemagne': 'Berlin', 
'Maroc': 'Rabat', 
'Espagne': 'Madrid', 
'Irak': 'Bagdad', 
'Italie': 'Rome' 
}

nv_dict = {}

for i,j in dictionnaire_pays_capitales.items():
    nv_dict.update({j:i})

print(nv_dict)