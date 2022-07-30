arr = [20,30,21,33,32,99]
minm=arr[0]
maxm=arr[0]
for i in range(len(arr)):
    if arr[i]<minm:
        minm = arr[i]
    if arr[i]>maxm:
        maxm = arr[i]
print(minm)
print(maxm)