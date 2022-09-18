a=[]
n= int(input("Enter the number:"))
for x in range(0,n):
    ele=int(input("Enter element" + str(x+1) + ":"))
    a.append(ele)
temp=a[0]
a[0]=a[n-1]
a[n-1]=temp
print(a)
