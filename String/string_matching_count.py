#Count the Number of matching characters in a pair of string

def count_matching_characters(s1, s2):
    # return len(set(s1) & set(s2))  # Using set intersection to count matching characters


    used = [False] * len(s2)
    count=0

    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j] and not used[j]:
                used[j] = True
                count+=1
                break
    return count


s1 = "VISHAKSHI"
s2 = "VANSHIKA"

ans = count_matching_characters(s1, s2)
print("The number of matching characters in the two strings is:", ans)