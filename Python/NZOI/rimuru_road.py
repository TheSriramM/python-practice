#old code (doesn't work)

# interval = input()
# #seperate the three numbers
# interval = interval.split()
# current_dist = int(input())
# dist_1 = 0
# dist_2 = 0
# dist_3 = 0
# smallest_no = 100000000000
# same_no = False


# dist_1 = current_dist % int(interval[0])
# dist_2 = current_dist % int(interval[1])
# dist_3 = current_dist % int(interval[2])
# higher_1 = (dist_1 + 2) * int(interval[0])
# higher_2 = (dist_2 + 2) * int(interval[1])
# higher_3 = (dist_3 + 2) * int(interval[2])
# higher_rem_1 = higher_1 - current_dist
# higher_rem_2 = higher_2 - current_dist
# higher_rem_3 = higher_3 - current_dist

# if a <= 1000000000 and b <= 1000000000 and c <= 1000000000:
#     if higher_rem_1 > 0:
#         if dist_1 > higher_rem_1:
#             dist_1 = higher_rem_1
#     if higher_rem_2 > 0:
#         if dist_2 > higher_rem_2:
#             dist_2 = higher_rem_2
#     if higher_rem_2 > 0:
#         if dist_3 > higher_rem_3:
#             dist_3 = higher_rem_3

# #find the smallest remainder
# smallest = [dist_1, dist_2, dist_3]
# for num in smallest:
#     if smallest_no != num:
#         if num < smallest_no:
#             smallest_no = num
#     else:
#         same_no = True

# if same_no == True:
#     print(smallest_no)
#     print("can't make up my mind")
# else:
#     print(smallest_no)

#new code (works)

a, b, c = map(int, input().split())
distance = int(input())
output = []

mod_a, mod_b, mod_c = distance % a, distance % b, distance % c
floor_a, floor_b, floor_c = distance // a, distance // b, distance // c
higher_a, higher_b, higher_c = floor_a + 1, floor_b + 1, floor_c + 1
high_rem_a, high_rem_b, high_rem_c = (higher_a * a) - distance, (higher_b * b) - distance, (higher_c * c) - distance

if mod_a < high_rem_a:
    output.append(mod_a)
else:
    output.append(high_rem_a)
if mod_b < high_rem_b:
    output.append(mod_b)
else:
    output.append(high_rem_b)
if mod_c < high_rem_c:
    output.append(mod_c)
else:
    output.append(high_rem_c)

print(min(output))
if output.count(min(output)) > 1:
    print("can't make up my mind")

#first hard problem solved on NZOI


