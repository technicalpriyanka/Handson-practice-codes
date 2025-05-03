#compund interest 
# A=p(1+r/100)^t
#ci=a-p

# p=10000
# r=8
# t=6

# a=p*(pow((1+r/100),t))
# ci=a-p
# print(ci)

#with function

def compund_func(p, t, r):
    print("**")
    a=p*(pow((1+r/100), t))
    print(a)
    print("&&&&")
    ci=a-p

    print("code exectuin ")
    return ci

print("value")
p, t, r = 10000,6,8

print("function calling")
ans =compund_func(p,t,r)

print("output flow")
print(ans)

# print("by taking input")

# def comp_func(p,t,r):
#     a=p*(pow((1+r/100), t))
#     ci=a-p
#     return ci

# p=int(input("enter principal amount"))
# t=int(input("enter duration in years"))
# r=int(input("enter rate "))

# ans= comp_func(p,t,r)
# print(ans)