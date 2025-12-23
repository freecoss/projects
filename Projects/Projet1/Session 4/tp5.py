produits = { 
'produit1': {'prix': 30, 'reduction': 10}, 
'produit2': {'prix': 30, 'reduction': 5}, 
'produit3': {'prix': 40, 'reduction': 10} 
}
final_price = 0
for i,j in produits.items():
        final_price += j["prix"]-(j["prix"]*(j["reduction"]/100))
        
print(final_price)