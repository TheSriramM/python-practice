t = int(input())
cups = []
pairs = []
unique = []
for _ in range(t):
    cups.append(int(input()))
cup_set = set(cups)
for item in cup_set:
    if cups.count(item) == 2:
        pairs.append(str(item))
        pairs.append(str(item))
    else:
        unique.append(str(item))

pairs = [int(item) for item in pairs]
unique = [int(item) for item in unique]
pairs.sort()
unique.sort()
pairs = [str(item) for item in pairs]
unique = [str(item) for item in unique]
print(f"Shelf 1: {" ".join(pairs)}")
print(f"Shelf 2: {" ".join(unique)}")