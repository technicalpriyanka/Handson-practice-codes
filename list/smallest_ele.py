def smallest_ele(my_list):
    min=my_list[0]
    max=my_list[0]

    for i in range(len(my_list)):

        if my_list[i] < min:
            min=my_list[i]

    
        #maximum element
        if my_list[i] > max:
            max=my_list[i]

    return min,max
    
    

    
        


my_list = [10, 20, 30, 1, 8, 40, 50]
ans=smallest_ele(my_list)

print(ans)