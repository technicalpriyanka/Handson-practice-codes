def interchange_ele(my_list):
    # ans=[]
    n=len(my_list)
    for i in range(len(my_list)):
        temp=my_list[0]
        my_list[0]=my_list[n-1]
        my_list[n-1]=temp


    return my_list

my_list = [1, 2, 3, 4, 5]

res=interchange_ele(my_list)
print(res)


print("another way")

my_list = [1, 2, 3, 4, 5]
my_list[0],my_list[-1] = my_list[-1], my_list[0]
print(my_list)