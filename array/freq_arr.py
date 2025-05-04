def frequency_checkup(arr):
    count=0

    for i in range(len(arr)):
        count+=1
    return count
arr = [10, 324, 45, 90, 9808, 5, 6, 7, 8, 1]
res=frequency_checkup(arr)
print(res)