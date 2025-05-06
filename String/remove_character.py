#removing ith character from string
def remove_ith_character(s, t):

    res=""
    for i in range(len(s)):
        if i != t:
            res+=s[i]           #adding except index t
    return res

s = "PythonProgramming"
t=4

#calling function
ans = remove_ith_character(s, t)
print("The string after removing the ith character is :", ans)