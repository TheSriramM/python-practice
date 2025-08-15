# https://codeforces.com/problemset/problem/2007/B

t = int(input())
output = []

for _ in range(t):
    n, m = map(int, input().split())
    array = sorted(list(map(int, input().split())))
    case_out = ""
    for _ in range(m):
        operation = input().split()
        largest = int(operation[2])
        smallest = int(operation[1])
        for i in range(n):
            if array[i] < smallest:
                continue
            if array[i] > largest:
                break
            if array[i] <= largest and array[i] >= smallest:
                if operation[0] == "+":
                    array[i] += 1
                else:
                    array[i] -= 1
        
        case_out += str((sorted(array)[-1])) + " "
    output.append(case_out)

for item in output:
    print(item)