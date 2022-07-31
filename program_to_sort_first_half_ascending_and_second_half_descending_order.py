lst = [1,90,34,89,7,9]
n = len(lst)
lst.sort()
arr = [0]
i=0
while i < n/2:
    print(lst[i])
    i = i+1
j=n-1
while j>=n/2:
    print(lst[j])
    j=j-1