n = int(input())
score = 10
for i in range(n):
    score += int(input())

if score == 10:
    print("She's got them all")
else:
    print(10-score)