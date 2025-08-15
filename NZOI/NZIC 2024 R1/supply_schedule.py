n = int(input()) # N = 2 Subtask attempt
a_schedule = list(map(int, input().split()))
b_schedule = list(map(int, input().split()))
potential = []

if max(b_schedule) >= max(a_schedule):
    largest_sch = b_schedule
    small_sch = a_schedule
else:
    largest_sch = a_schedule
    small_sch = b_schedule


for i in range(max(largest_sch)):
    first = largest_sch[0] - i
    second = largest_sch[1] - i
    cur_score = 0
    if first != small_sch[0]:
        cur_score += 2
    if second != small_sch[1]:
        cur_score += 2
    potential.append(cur_score)

if potential:
    print(min(potential))
else:
    print(0)