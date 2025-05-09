a = [("name", "Alice"), ("age", 25), ("city", "New York")]

print(dict(a))

b = {}
for key, value in a:
    b[key] = value

print(b)