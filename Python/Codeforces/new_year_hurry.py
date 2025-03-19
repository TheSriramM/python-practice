#get two integers n and k
#time left = 240
#n = last question
#k = time to go to house


n, k = map(int, input().split())
output = 0
q_solve_time = 0
t_left = 240
t_left -= k
for i in range(1, n+1):
    i *= 5
    q_solve_time += i
    if q_solve_time <= t_left:
        output += 1
print(output)

#correct