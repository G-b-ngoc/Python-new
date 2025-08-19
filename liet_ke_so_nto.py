import math
# Bài tập: Kiểm tra số nguyên tố
def nt(n):
    if n < 2: return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
for i in range(1, n + 1):
    if nt(i):
        print(i, end = ' ')