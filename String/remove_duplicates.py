# Remove All Duplicates from a Given String 
def remove_duplicates(s):
    seen = set()
    result=""
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    return result

s = "geeksforgeeks"
ans= remove_duplicates(s)
print("The string after removing duplicates is:", ans)