n = int(input())
output = []
for i in range(n):
    word = input().strip()
    if len(word) > 10:
        output.append(word[0] + str(len(word) - 2) + word[-1])
    else:
        output.append(word)
for item in output:
    print(item)