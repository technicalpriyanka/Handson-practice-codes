#spliting the string and joining the string
def split_join_string(str):

    words =str.split(" ")# #splitting the string into words
    res="*".join(words)

    return res


str="The goal here is to split a string into smaller parts based on a delimiter and then join them back together."

ans= split_join_string(str)
print("The string after splitting and joining is:", ans)

# print("The original string is:", str)