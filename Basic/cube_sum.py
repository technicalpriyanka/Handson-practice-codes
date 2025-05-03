def cubesum(n):
    ans=0
    for i in range(1, n+1):
        ans=ans+(i*i*i)
    return ans

n=4
print(cubesum(n))


