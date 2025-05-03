def count_num(a):
    even_num=0
    odd_num=0

    for i in range(len(a)):
        if a[i] %2==0:
            even_num+=1

        else:
            odd_num+=1

    return "count of even numbers",even_num, "count of odd numbers", odd_num

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ans=count_num(a)

print(ans)