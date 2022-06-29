lst = [1,3,5,8,6,5,2]
n=len(lst)
for i in range(0,n-1):
    if(lst[i]<lst[i+1] and lst[i+2]<lst[i+1]):
         print(lst[i+1])