# Create a List of Tuples with Numbers and Their Cubes
a = [1, 2, 3, 4, 5]


for i in a:
    print((i, i**3), end=" ")

print("\nanother way")
res=[]
for k in a:
    res.append((k, k**3))
print(res) #output: [(1, 1), (2, 8), (3, 27), (4, 64), (5, 125)]