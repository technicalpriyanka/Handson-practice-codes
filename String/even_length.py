#program to print even length words in a string

def even_length_words(s):
    word = s.split()
    result = []
    for i in word:
        if len(i)%2 == 0:
            # print(i, end= " ")
            result.append(i)

    return result

    

s = "My name is shakshi and I am a student"
ans=even_length_words(s)
print(ans)


