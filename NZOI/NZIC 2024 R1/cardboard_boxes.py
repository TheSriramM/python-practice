#https://train.nzoi.org.nz/problems/1371

box_no = int(input())
boxes = []
for box in range(box_no):
    width = int(input())
    boxes.append(width)
print(len(set(boxes)))
