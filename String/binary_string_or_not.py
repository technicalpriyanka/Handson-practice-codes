#checking string is binary or not
import re 


s = "101010000111"
if set(s).issubset({'0','1'}):
    print("The string is binary")
else:
    print("The string is not binary")

def is_binary_string(s):
    for char in s:
        # if char not in '01':
        if char != '0' and char != '1':
            return False
    return True

s = "101010000111"

ans=is_binary_string(s)
print("The string is binary" if ans else "The string is not binary")

# if re.match("^[01]+$", s):
#     print("The string is binary")   
# else:
#     print("The string is not binary")

