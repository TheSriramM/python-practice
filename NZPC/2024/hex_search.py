n = int(input())
non_hex = ""
output = []
for _ in range(n):
    row = input().split()
    sum = ""
    for item in row:
        if item in "0123456789ABCDEF":
            sum += item
        else:
            non_hex += item
            if len(sum) > 0:
                output.append(str(int(sum, 16)))
            sum = ""
    if len(sum) > 0:
        output.append(str(int(sum, 16)))
if len(non_hex) > 0:
    print(non_hex)
for item in output:
    print(item)