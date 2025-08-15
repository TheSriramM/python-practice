dragons, knights = map(int, input().split())
dragon_list = []
knight_list = []
impossible = False
cost = 0
for _ in range(dragons):
    dragon_list.append(int(input()))

for _ in range(knights):
    knight_list.append(int(input()))

if dragons > knights:
    print("Loowater is doomed!")
else:
    for item in dragon_list:
        strong = [knight for knight in knight_list if knight >= item]
        if len(strong) != 0:
            smallest = min(strong)
            cost += smallest
            knight_list.remove(smallest)
        else:
            impossible = True
if impossible:
    print("Loowater is doomed!")
else:
    if cost != 0:
        print(cost)