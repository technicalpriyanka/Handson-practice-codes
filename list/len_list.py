# Ways to find length of list

def freq_list(my_list):

    count=0

    for i in range(len(my_list)):
        # count+=my_list[i]         to fetch sum of all elements from list
        count+=1                #for count of list
        

    return count


my_list = [1, 2, 3, 4, 5]

ans=freq_list(my_list)

print(ans)