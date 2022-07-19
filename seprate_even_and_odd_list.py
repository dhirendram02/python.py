lst = [5,4,8,7,9,13,12,55,60]
even = [] 
odd = [] 
for i in lst:
    if (i % 2 == 0): 
        even.append(i) 
    else:
        odd.append(i) 
print("Even list:", even) 
print("Odd list:", odd) 