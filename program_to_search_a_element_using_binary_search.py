def binary_search(arr,search):
    s=0
    end=len(arr)-1
    while(s<=end):
        mid=(s+end)//2
        if arr[mid]<search:
            s=mid+1
        elif arr[mid]>search:
            end=mid-1
        else:
            return mid
    return -1
arr=[2,3,4,5,6,0]
search=int(input())
idx=binary_search(arr,search)
if idx== -1:
    print("element is not present")
else:
    print("element is present at index ", str(idx))
