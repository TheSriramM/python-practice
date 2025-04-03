# no_of_inputs_1 = input()
# inputs_1 = input()
# no_of_inputs_2 = input()
# inputs_2 = input()
# no_of_inputs_3 = input()
# inputs_3 = input()

# #variables
# average_1 = 0
# average_2 = 0
# average_3 = 0
# resow_count = 0
# no_of_inputs_1 = int(no_of_inputs_1)
# no_of_inputs_2 = int(no_of_inputs_2)
# no_of_inputs_3 = int(no_of_inputs_3)

# #no_of_inputs_x takes the number of inputs it will receive for that year
# #inputs_x takes the data for the year

# inputs_1 = inputs_1.split()
# inputs_2 = inputs_2.split()
# inputs_3 = inputs_3.split()

# for item in inputs_1:
#     item = int(item)
#     average_1 += item
# average_1 = average_1 / no_of_inputs_1

# for item in inputs_2:
#     item = int(item)
#     average_2 += item
# average_2 = average_2 / no_of_inputs_2

# for item in inputs_3:
#     item = int(item)
#     average_3 += item
# average_3 = average_3 / no_of_inputs_3

# if average_1 >= 12 and average_2 >= 12 and average_3 >= 12:
#     for item in inputs_3:
#         item = int(item)
#         if item >= 25:
#             resow_count += 1
#     if resow_count / no_of_inputs_3 >= 0.5:
#         print("resow")
#     else:
#         print("unhealthy")
# else:
#     print("healthy")

data_1, percentage_1 = int(input()), list(map(int, input().split()))
data_2, percentage_2 = int(input()), list(map(int, input().split()))
data_3, percentage_3 = int(input()), list(map(int, input().split()))
count = 0
#calculate the sum of each item in the list
add_1, add_2, add_3 = sum(percentage_1), sum(percentage_2), sum(percentage_3)
avg_1, avg_2, avg_3 = (add_1 / data_1), (add_2/ data_2), (add_3 / data_3)
if avg_1 >= 12 and avg_2 >= 12 and avg_3 >= 12:
    resow_percent = data_3 // 2
    for item in percentage_3:
        if item >= 25:
            count += 1
    if count > resow_percent:
        print("resow")
    else:
        print("unhealthy")
else:
    print("healthy")

