x, y = map(int, input().split())
total = 0
locations = {}
for _ in range(int(input())):
    coord = " ".join(input().split())
    if coord in locations:
        locations[coord] += 1
    else:
        locations[coord] = 1
for _ in range(int(input())):
    search = " ".join(input().split())
    if search in locations:
        total += locations[search]
print(total)