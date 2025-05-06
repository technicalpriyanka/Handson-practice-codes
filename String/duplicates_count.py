#count the double characters in a string

from collections import Counter
# Count the occurrences of each character in the string.
s = "GeeksforGeeks"
count = Counter(s)
for cnt in count.items():
    if cnt[1] > 1:
        print(cnt[0], cnt[1])




#************************************************
s = "GeeksforGeeks"
res = []
for char in set(s):
    if s.count(char) > 1:
        res.append(char)
print(res)