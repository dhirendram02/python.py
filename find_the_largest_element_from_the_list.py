lst = [2,9,4,6,12,1,5]

lar = lst[0]

for num in lst:
    if num > lar:
        lar = num
        
print(lar)