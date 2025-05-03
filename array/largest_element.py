def max_ele(arr):

    max=arr[0] #initialize
    print("ms",max)

    for i in range(1, len(arr)):
        print("data")
        if arr[i] > max:
            print("asdf")
            max = arr[i]
            print("***********************")
            print("maximum", max)
    return max

arr = [10, 324, 45, 90, 9808]

res=max_ele(arr)
print(res)





print("%%%%%%%%%%%%%%%%%%%%%%%%%%% another way by sorting %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

def larget_elemen(arr):

    arr.sort()
    n=len(arr)
    for i in range(n):
        return arr[n-1]
    
arr=[2, 3, 4, 5, 6, 7, 8, 1]

ans=larget_elemen(arr)
print(ans)
