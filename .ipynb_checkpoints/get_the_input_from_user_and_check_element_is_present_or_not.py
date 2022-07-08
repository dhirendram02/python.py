i = 10
a = []
while i>0:
    num = 1,3,44,22,55,99,66,88,32,45
    a.append(num)
    i = i-1
n = 55
i = 9
count = 0
while i>=0:
    if n == a[i]:
        print ("Yes")
        count = count + 1
    i = i-1
if count == 0:
    print ("No")