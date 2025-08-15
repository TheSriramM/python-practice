n = int(input())
output = []

for _ in range(n):
    x, y = map(int, input().split())
    if x % 2 == 0 and y % 2 == 0:
        output.append("BLACK")
    elif (x % 2 == 0 and y % 2 == 1) or (x % 2 == 1 and y % 2 == 0):
        output.append("WHITE")
    else:
        output.append("BLACK")

for item in output:
    print(item)