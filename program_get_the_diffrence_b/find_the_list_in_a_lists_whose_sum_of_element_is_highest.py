num = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
 
idx = 0
max= 0
sum_max = 0
for list in num:
    sum_list = 0
    for x in list:
        sum_list += x
    if sum_list > sum_max:
        sum_max = sum_list
        max = idx
    idx += 1
 
print(num[max])