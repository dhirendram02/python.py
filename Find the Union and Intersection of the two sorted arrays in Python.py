def union(list1, list2):
    list1 = set(list1)
    list2 = set(list2)
    print("List 1= ", list1)
    print("List 2= ", list2)
    print("Union of two list: ", list1 | list2)


def intersection(list1, list2):
    list1 = set(list1)
    list2 = set(list2)
    print("Intersection of two list: ", list1 & list2)

list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]

union(list1, list2)
intersection(list1, list2)
