a=[]
n= int(input("enter the number :"))
for x in range(0,n):
    ele=input(" element" + str(x+1) + ":")
    a.append(elem)
max1=len(a[0])
temp=a[0]
for i in a:
    if(len(i)>max1):
       max1=len(i)
       temp=i
print(" the longest length:")
print(temp)
