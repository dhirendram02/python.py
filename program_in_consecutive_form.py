#program in consecutive form.
lst = [1,2,3,4,5,6,11,15,16,1,17,18,19,11,20,21,22,23]
temp = []
out = []
for i in range(0,len(lst)-1):
    if(lst[i]+1 == lst[i+1]):
        temp.append(lst[i])
    else:
        temp.append(lst[i])
        out.append(temp)
        temp = []
temp.append(lst[i+1])
out.append(temp)
temp = []
print(out)