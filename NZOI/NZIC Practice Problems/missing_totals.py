t = int(input())
output = []

for _ in range(t):
    price , discount = map(int, input().split())
    if price - discount > 0:
        output.append(price-discount)

print(sum(output))