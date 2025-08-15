n = int(input())
towers = list(map(int, input().split()))

for i in range(n):
    unsafe = 0
    for j in range(1, n):
        if i != j:
            if towers[i] < towers[j]:
                unsafe += 1
                break
            else:
                for k in range(i, j+1):
                    if towers[k] > towers[i]:
                        unsafe += 1
                        break
        else:
            break

    print(unsafe)