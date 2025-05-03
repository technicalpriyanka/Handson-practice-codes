def palindrome(*str1):

    res=[]
    for i in str1:
        s=str(i)
        if s==s[::-1]:
            res.append((i, True))
        else:
            res.append((i, False))
    
        
    return res




str1=["Racecar", 121]

ans=palindrome(*str1)
print(ans)