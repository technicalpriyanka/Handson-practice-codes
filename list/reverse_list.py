def reverse_lis(my_list):
    
    for i in range(len(my_list)):
        my_list=my_list[::-1]

    return my_list



my_list = [10, 20, 30, 40, 50]

ans=reverse_lis(my_list)

print(ans)