List1= [3,4,5,3,4,5,1,1,1,1] 
print(List1)
for i,ref_i in enumerate(List1):
    for j,ref_j in enumerate(List1):
        if ref_i == ref_j and i!=j:
            List1.pop(i)
    
    
print(List1)
