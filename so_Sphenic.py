import math
def sp(n):
    cnt = 0
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            mu = 0
            while n % i == 0:
                mu += 1
                n //= i
            if mu >= 1:
                return False
            cnt += 1
    if n > 1:
        cnt += 1
    return cnt == 3

n = int(input())
if sp(n):
    print(1)
else:
    print(0)