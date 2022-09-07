def sequential_search(lst, item):

    pos = 0
    found = False
    
    while pos < len(lst) and not found:
        if lst[pos] == item:
            found = True
        else:
            pos = pos + 1
    
    return found, pos

print(sequential_search([11,23,58,31,56,77,43,12,65,19],31))
