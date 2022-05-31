#staircase search
list=[2,3,4,5,6,7,8]
#search=int(input())
search=33
first=0              
last=len(list)-1     
mid=(first+last)//2

while first<=last:
    if list[mid]<search:        
        low=mid+1                     
    elif list[mid]==search:     
        print("number is found at index")
        break
    else:
        last=mid-1
    mid=(first+last)//2
    if (first>last):
        print("number not found in list")  