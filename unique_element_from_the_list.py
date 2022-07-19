lst = [3,4,4,1,2,3,2,1]
b=[]
for i in lst:
    if i not in b:
        b.append(i)
print(b)