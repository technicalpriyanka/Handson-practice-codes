#area of circle =pi*r*r

r=23
pi=3.14

import math 
print(math.pi)

area_circle= pi * r * r
print(area_circle, "area of circle")

def area_cir(pi, r):
    area = pi* r* r
    return area

pi=3.14
r=23

ans=area_cir(pi, r)
print(ans)
