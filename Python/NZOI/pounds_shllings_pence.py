n, lines = int(input()), int(input())
pounds = 0
shillings = 0
pence = 0
for i in range(lines):
    money = input().split("-")
    money[0] = money[0].replace("#", "")
    pounds += int(money[0])
    shillings += int(money[1])
    pence += int(money[2])
    pounds += shillings // 20
    shillings += pence // 20
    pence %= 12
    shillings %= 20
print(f"#{pounds}-{shillings}-{pence}")

