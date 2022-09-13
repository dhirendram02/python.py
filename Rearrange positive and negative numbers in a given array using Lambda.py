array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
print(array_nums)
result = sorted(array_nums, key = lambda i: 0 if i == 0 else -1 / i)
print(result)
