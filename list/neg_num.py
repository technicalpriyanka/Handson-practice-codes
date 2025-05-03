def check_negative(a):
    res=[]

    for i in range(len(a)):
        if a[i] < 0:
            res.append(a[i])

    return res

a = [-10, 15, 0, 20, -5, 30, -2]

ans = check_negative(a)
print(ans)