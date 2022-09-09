def first_duplicate(nums):
    num_set = set()
    no_dup = -1

    for i in range(len(nums)):

        if nums[i] in num_set:
            return nums[i]
        else:
            num_set.add(nums[i])

    return no_dup

print(first_duplicate([1, 2, 3, 4, 4, 5]))
print(first_duplicate([1, 2, 3, 4]))
print(first_duplicate([1, 1, 2, 3, 3, 2, 2]))
