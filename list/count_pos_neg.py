def count_numbers(a):
    pos=0
    neg=0
    zero=0

    for i in range(len(a)):
        if a[i] > 0:
            pos+=1
        elif a[i] < 0:
            neg+=1
        else:
            zero+=1

    return pos, neg, zero

a = [-10, 15, 0, 20, -5, 30, -2]
ans= count_numbers(a)
print(ans)