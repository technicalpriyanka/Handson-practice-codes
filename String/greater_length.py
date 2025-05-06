def string_greater_than_length(str, k):
    res=[]
    text=str.split(" ")
    for i in text:
        if len(i)>k:
            res.append(i)
    return res

str = "hello geeks for geeks is computer science portal" 
k=4

ans= string_greater_than_length(str, k)
print(len(ans))
print("The words in the string greater than length k are:", ans)

