from math import *
def tong(n):
    tong = 0
    while n != 0:
        tong += n % 10
        n //= 10
    return tong

def check(n):
    sum1 = tong(n)
    sum2 = 0
    temp = n
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            while n % i == 0:
                sum2 += tong(i)
                n //= i
    if temp == n:
        return False #N la so nto
    if n > 1:
        sum2 += tong(n)
    return sum1 == sum2

n = int(input())
if check(n):
    print('YES')
else:
    print('NO')