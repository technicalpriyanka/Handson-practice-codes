def replace_multiple_words_with_k(s, list_words, k):


    for i in s.split():
        if i in list_words:
            s = s.replace(i, k)

    return s

s = 'Geeksforgeeks is best for geeks and CS'
list_words = ['geeks', 'CS', 'best']
k = "GFG"

ans= replace_multiple_words_with_k(s, list_words, k)
print(ans)
# print(s)