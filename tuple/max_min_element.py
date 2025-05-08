# Maximum and Minimum K elements in Tuple
test_tup = (5, 20, 3, 7, 6, 8) #output: (3,5,8,20)
k = 2 

sorted_tup = sorted(test_tup)
list_val = list(sorted_tup)

print(list_val)
res = []

for idx, val in enumerate(list_val):
    if idx < k or idx >= len(list_val) - k:
        res.append(val)

res = tuple(res)
print(res) #output: (3, 5, 8, 20)
# minimum and maximum k elements in tuple

