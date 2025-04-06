"""Try to check each hut starting location for clockwise and anti clockwise
W_next = W_current + total_sum - N * A[i]

W_current: the weighted sum for the current rotation

W_next: the weighted sum for the next rotation (one step clockwise)

total_sum: the sum of all difficulty ratings, i.e., sum(A)

A[i]: the element that’s at the front of the array in the current rotation, and will move to the back in the next rotation

N: the number of elements (length of the array)"""


n = int(input())
difficulty = list(map(int, input().split()))
clockwise_n, anticlockwise_n = n,n
add = 0
total_sum = sum(difficulty)
values = []
w0 = []
wi = []

#code for w0 which is the weighted sum of the original order
for item in difficulty:
    w0.append(item * clockwise_n)
    clockwise_n -= 1
wi = sum(w0)
values.append(wi)
first = difficulty[0]


#try to find the next orders for clockwise rotation
for i in range(n):
    add += 1
    clockwise_n = n
    wi += total_sum - len(difficulty) * first
    values.append(wi)
    first = add
print(values)

#algorithm has a bug