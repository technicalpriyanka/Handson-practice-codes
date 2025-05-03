def find_even(a):
    res=[]
    for i in range(len(a)):
        if a[i] % 2 == 0:
            # print(a[i])
            res.append(a[i])

    return res



a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ans=find_even(a)
print(ans)