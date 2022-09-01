def find(arr1, arr2, arr3):
    print("common element  ", end="")
    arr1 = set(arr1)
    arr2 = set(arr2)
    arr3 = set(arr3)
    print(arr1 & arr2 & arr3)


array1 = [1, 2, 3, 4]
array2 = [3, 4, 5, 6]
array3 = [3, 5, 6, 7]

print("Array1 = ", array1)
print("Array2 = ", array2)
print("Array3 = ", array3)

find(array1, array2, array3)
