def remove_empty_tuples(a):
    res=[]
    for i in range(len(a)):
        if a[i] != ():
            res.append(a[i])
    return res

a = [(1, 2), (), (3, 4), (), (5,)]

ans = remove_empty_tuples(a)

print(ans)