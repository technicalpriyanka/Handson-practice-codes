def ele_exists(my_list):
    n=30

    for i in range(len(my_list)):

        if my_list[i] == n:
            return True
    return False                # Only return False after checking all elements


my_list = [10, 20, 30, 40, 50]

ans = ele_exists(my_list)

print(ans)