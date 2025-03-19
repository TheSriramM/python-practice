n = int(input())
output = []
implement = 0
for i in range(n):
    problem = input().split()
    if problem.count("1") > 1:
        implement += 1
    
print(implement)

#correct