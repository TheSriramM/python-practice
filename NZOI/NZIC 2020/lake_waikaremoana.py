n = int(input())
difficulty = list(map(int, input().split()))
difficulty.sort()
add = 0
for dif in difficulty:
    add += dif * n
    n -= 1
print(add)