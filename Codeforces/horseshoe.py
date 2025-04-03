shoes = input().split()
need_to_buy = 0
shoe_1, shoe_2, shoe_3, shoe_4 = shoes.count(shoes[0]), shoes.count(shoes[1]), shoes.count(shoes[2]), shoes.count(shoes[3]) 
repeat_list = [shoe_1, shoe_2, shoe_3, shoe_4]
for item in repeat_list:
    if item == 1:
        repeat_list.remove(item)
    elif item == 2:
        need_to_buy += 1
        break
    elif item == 3:
        need_to_buy += 2
        break
    else:
        need_to_buy += 3
        break
print(need_to_buy)