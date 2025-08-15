matches = []
indexes = []
total = 0

for _ in range(8):
    matches.append(input())

for i in range(8):
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        total += 2
    elif x == y:
        total += 3
        indexes.append(i)
    else:
        total += 1

print(f"Points scored: {total}")
if len(indexes) == 0:
    print("No scoring draws")
else:
    for i in range(8):
        if i in indexes:
            print(matches[i])