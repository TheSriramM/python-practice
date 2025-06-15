#https://codeforces.com/problemset/problem/1883/C

import math

cases = int(input())
output = []
for case in range(cases):
    size, product = map(int, input().split())
    nums = list(map(int, input().split()))
    cur_product = math.prod(nums)
    if product % cur_product == 0:
        output.append(0)
    else:
        print(cur_product % product)