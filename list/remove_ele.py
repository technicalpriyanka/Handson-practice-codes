def remove_element(lst, element):

    # for i in range(len(lst)):
    #     if i not in element:
    #         lst.remove(i)

    # return lst 

    res = []
    for i in range(len(lst)):
        if lst[i] not in element:
            res.append(lst[i])

    return res

lst = [10, 20, 30, 40, 50, 60, 70]
element = [20, 40, 60]

ans = remove_element(lst, element)
print(ans)