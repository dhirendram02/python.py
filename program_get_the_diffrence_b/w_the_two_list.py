l1 = [1,5,3,4,6,8]
l2 =[2,1,5,4,9,11]
a = list(set(l1) - set(l2))
b = list(set(l2) - set(l1))
sums=a+b
print(sums)