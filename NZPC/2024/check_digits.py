id = input()
while id != "0":
    summed = 0
    index = 1
    for num in id[::-1]:
        index += 1
        summed += index * int(num)
    rem = summed % 11
    final = 11 - rem
    if final >= 1 and final <= 9:
        new_id = id + str(final)
    elif final == 11:
        new_id = id + str(0)
    else:
        new_id = "rejected"
    print(f"{id} -> {new_id}")
    id = input()