#https://train.nzoi.org.nz/problems/19

steps = 0
values = []
while True:
    num = int(input())
    if num == 0:
        break
    while num != 1:
        if num % 2 == 0:
            num /= 2
            steps += 1
        else:
            num *= 3
            num += 1
            steps += 1
    values.append(steps)
    steps = 0
for item in values:
    print(item)