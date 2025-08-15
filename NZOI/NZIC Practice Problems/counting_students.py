# https://train.nzoi.org.nz/problems/35

t = int(input())
nums = []
dup=[]

for _ in range(t):
    n = int(input())
    if n not in nums:
        nums.append(n)
    else:
        dup.append(n)

for item in sorted(dup):
    print(item)