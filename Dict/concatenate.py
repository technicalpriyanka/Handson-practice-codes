d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}

d1.update(d2)

print(d1)

print(d1 | d2)

d3={**d1, **d2}
print(d3)


d3 = d1.copy()
for key, value in d2.items():
    d3[key] = value

print(d3)
# d1.copy() creates a shallow copy of d1 to preserve the original dictionary.
# for loop iterates through each key-value pair in d2 and adds or updates it in d3.
