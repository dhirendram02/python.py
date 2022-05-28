arr = [1,2,222,44,54,46,99,-2,-3]
ans=0
i=1
while i<len(arr)-1:
    ispeak = arr[i]>arr[i-1] and arr[i]>arr[i+1]
    if ispeak:
        cnt=1
        j=i
        while j>0 and arr[j-1]<arr[j]:
            cnt +=1
            j -= 1
        j=i