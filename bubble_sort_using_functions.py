# Bubble sort in Python

def bs(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp


lst = [-2, 45, 0, 11, -9]
bs(lst)
print(lst)