from collections import Counter

def word_frequency(s):
    word=s.split(" ")
    word_count = Counter(word)
    return word_count


s = "hello world hello everyone"
ans= word_frequency(s)
print(ans)

#with dictionary
s = "hello world hello everyone"
word_frequency = {}

for word in s.split(" "):
    word_frequency[word] = word_frequency.get(word, 0)+1

print(word_frequency)
#with dictionary comprehension
