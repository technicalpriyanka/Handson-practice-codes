#swapping ekement of 2 to 4
def swap_ele(my_list):

    n=len(my_list)
    for i in range(len(my_list)):
        temp=my_list[2]
        my_list[2]=my_list[4]
        my_list[4]=temp

    return my_list


my_list = [10, 20, 30, 40, 50]

ans=swap_ele(my_list)
print(ans)