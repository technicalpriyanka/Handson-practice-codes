d = {'a': 100, 'b': 200, 'c': 300}

res = sum(d.values())
print(res)
# d = {'a': 100, 'c': 455, 'd': 789}

ans= 0
for value in d.values():
    ans+=value

print(ans, "sum of all values ")
