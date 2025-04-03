no_of_times = int(input())
output = []
for i in range(1, no_of_times + 1):
    n = int(input())
    combinations = []
    b = n
    a = 0
    while b != 1:
        b -= 1
        a += 1
        combinations.append([a, b])
    output.append(len(combinations))
for item in output:
    print(item)

    #lesgooo first codeforces problem correct first try
    