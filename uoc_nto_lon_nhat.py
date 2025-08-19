from math import *
def uoc(n):
    s = -1 
    for i in range(2, isqrt(n), +1):
        if n % i == 0:
            s = i
            while n % i == 0:
                n //= i
    if n > 1:
        s = n
    return s

tc = int(input())
for i in range(tc):
    n = int(input())
    print(uoc(n))