def check_anagram(str1, str2):

    if sorted(str1) == sorted(str2):
        return True
    return False


str1 = "listen"
str2 = "silent"

ans = check_anagram(str1, str2)

print(ans)
