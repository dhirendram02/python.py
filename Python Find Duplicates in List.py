my_list = [1, 3, 7, 1, 2, 7, 5, 3, 8, 1]
print('List:', my_list)
dup_item = {x for x in my_list if my_list.count(x) > 1}
print('Duplicate Elements:', dup_item)
