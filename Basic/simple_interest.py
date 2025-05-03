#simple interest = (p*t*r)/100

#while defining function thier are 3 ways /steps 
# 1.define function
# 2.provide values
# 3.function calling


#function defining
def fun(p,t,r):
    return (p*t* r)/100

#values
p,t,r= 100, 2,8

#FUNCTION CALLING
res = fun(p,t,r)

print(res)

print("alternate method")


#simpliy 
p,t,r= 100, 2,8

si=(p*t*r)/100
print(si)

print("***")


def new_func(a, b):
    return (a+b)

a,b = 10,20

ans=new_func(a,b)
print(ans)

# print(new_func(a,b))
