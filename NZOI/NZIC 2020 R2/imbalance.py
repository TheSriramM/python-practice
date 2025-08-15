# Passes some tests

# t, limit = map(int, input().split())
# boxes = list(map(int, input().split()))
# count = 0
# while count < limit:
#     count += 1
#     largest = max(boxes)
#     smallest = min(boxes)
#     large_index = boxes.index(largest)
#     small_index = boxes.index(smallest)
#     boxes[small_index] = smallest + 1
#     boxes[large_index] = largest - 1
# print(max(boxes)-min(boxes))

t, limit = map(int, input().split())
boxes = sorted(list(map(int, input().split())))
while limit > 0:
    limit -= 1
    boxes[-1] -= 1
    boxes[0] += 1
    boxes.sort()

print(max(boxes) - min(boxes))