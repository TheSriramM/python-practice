import math

t = int(input())

for _ in range(t):
    a, b, k = map(int, input().split())
    greatest = math.gcd(a, b)
    if  a//greatest <= k and b//greatest <= k:
        print(1)
    else:
        print(2)