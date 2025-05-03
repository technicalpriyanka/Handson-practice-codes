def mult_list(my_list):
    count=1

    for i in range(len(my_list)):
        count*=my_list[i]

    return count


my_list = [10, 20, 30, 40, 50]
ans=mult_list(my_list)

print(ans)