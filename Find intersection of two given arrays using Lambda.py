arr1 = [1, 2, 3, 5, 7, 8, 9, 10]
arr2 = [1, 2, 4, 8, 9]
print(arr1)
print(arr2)
res = list(filter(lambda x: x in arr1, arr2)) 
print ("Intersection ",res)
