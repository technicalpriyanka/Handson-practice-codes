def second_large(my_list):
    my_list.sort()

    n=len(my_list)
    return my_list[n-2]
    # res=[]
    # max=my_list[0]

    # for i in range(len(my_list)):
    #     if my_list[i] > max:
    #         max=my_list[i]
    #         res.append(max)

    # return [len(res)-2]


my_list = [10, 20, 60, 30, 40, 50]
ans=second_large(my_list)
print(ans)