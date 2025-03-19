no_of_inputs_1 = input()
inputs_1 = input()
no_of_inputs_2 = input()
inputs_2 = input()
no_of_inputs_3 = input()
inputs_3 = input()

#variables
average_1 = 0
average_2 = 0
average_3 = 0
resow_count = 0
no_of_inputs_1 = int(no_of_inputs_1)
no_of_inputs_2 = int(no_of_inputs_2)
no_of_inputs_3 = int(no_of_inputs_3)

#no_of_inputs_x takes the number of inputs it will receive for that year
#inputs_x takes the data for the year

inputs_1 = inputs_1.split()
inputs_2 = inputs_2.split()
inputs_3 = inputs_3.split()

for item in inputs_1:
    item = int(item)
    average_1 += item
average_1 = average_1 / no_of_inputs_1

for item in inputs_2:
    item = int(item)
    average_2 += item
average_2 = average_2 / no_of_inputs_2

for item in inputs_3:
    item = int(item)
    average_3 += item
average_3 = average_3 / no_of_inputs_3

if average_1 >= 12 and average_2 >= 12 and average_3 >= 12:
    for item in inputs_3:
        item = int(item)
        if item >= 25:
            resow_count += 1
    if resow_count / no_of_inputs_3 >= 0.5:
        print("resow")
    else:
        print("unhealthy")
else:
    print("healthy")
