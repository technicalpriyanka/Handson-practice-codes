def odd_num(a):
    res=[]
    for i in range(len(a)):
        if a[i]%2==1:
            res.append(a[i])

    return res

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ans=odd_num(a)
print(ans)