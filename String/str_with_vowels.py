# Program to Accept the Strings Which Contains all Vowels

def check_vowels(s):

    if vowels.issubset(set(s.lower())):
        return True
    else:
        return False
    # s=s.lower()
    # if len(s) < 5:
    #     return False
    # for char in s.lower():
    #     if char in vowels:
    #         return True
    # return False


s = "Geeksforgeeks"
vowels = set("aeiou")


ans=check_vowels(s)
print(ans)