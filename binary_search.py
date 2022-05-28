list = [2,3,4,5,6,7,8]
search= 4
s=0
end=len(list)-1
mid=(s+end)//2
while s<=end:
    if list[mid]<search:
        low = mid+1
    elif list[mid]==search:
        print("number found")
        break
    else:
        end = mid-1
    mid=(s+end)//2
    if(s>end):
        print("number is not found")
