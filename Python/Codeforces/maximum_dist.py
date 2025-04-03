"""Formula for finding the euclidean distance squared
    d^2"= (x2 - x1)^2 + (y2 - y1)^2
    
    Sample input:
    3
    321 -15 -525
    404 373 990

    points = (321, 404), (-15, 373), (-525, 990)
"""

import math
n = int(input())
x_values = input().split()
y_values = input().split()
index = 0
points = [[x_values[i], y_values[i]] for i in range(n)]
output = []
for item in points:
    index = points.index(item)
    if (len(points) - 1) != index:
        item = [int(item) for item in item]
        points[index+1] = [int(num) for num in points[index+1]]
        distance = math.dist(item, points[index+1])
        if len(output) > 1:
            if distance > output[0]:
                output.remove(output[0])
                output.append(distance)
        else:
            output.append(distance)
    else:
        break
print(max(output) ** 2)
