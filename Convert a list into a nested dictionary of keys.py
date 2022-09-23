num_list = [1, 2, 3, 4]
new_dict = curr = {}
for name in num_list:
    curr[name] = {}
    curr = curr[name]
print(new_dict)
