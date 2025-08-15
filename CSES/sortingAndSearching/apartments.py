n, m, k = map(int, input().split())
people= list(map(int, input().split()))
ap = list(map(int, input().split()))

count = 0

for apart in ap:
    for peop in people:
        if apart <= peop+k and apart >= peop-k:
            count += 1
            break

print(count)