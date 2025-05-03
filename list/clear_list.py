def clear_list(my_list):

    # a= my_list.clear()
    # return a                              #will give u None output


    for i in range(len(my_list)):
        my_list.pop()

    return my_list



my_list = [10, 20, 30, 40, 50]

ans = clear_list(my_list)

print(ans)