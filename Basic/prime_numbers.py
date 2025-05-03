x, y = 1, 100 #defining range

res = [] #list to store prime numbers

for n in range(x, y+1):
    if n <= 1:
        continue #for non prime

    is_prime=True   #assuming i is prime

    for i in range(2, int(n**0.5)+1):
        if n %i == 0:
            is_prime = False
            break

    if is_prime:
        res.append(n)




# res = []  # list to store primes

# for n in range(x, y + 1):
#     if n <= 1:
#         continue  # skip non-primes <= 1

#     is_prime = True  # assume n is prime
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             is_prime = False  # n is not prime
#             break

#     if is_prime:
#         res.append(n)  # add prime number
if res:
    print(res)
else:
    print("No")