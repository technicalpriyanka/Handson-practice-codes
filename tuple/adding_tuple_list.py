# Adding Tuple to List and Vice – Versa
a = [1, 2, 3]  # list
b = (4, 5)     # tuple
c = [6, 7] 

a.extend(b)
print(a) #output: None


ans = b + tuple(a)
print(ans)