sale_no, bag_size = map(int, input().split())
knives = list(map(int, input().split()))
output = []
knives.sort()
knives.reverse()
index = 0
for i in range(bag_size):
    output.append(knives[index])
    index += 1
print(sum(output))

#passed 100% of tests