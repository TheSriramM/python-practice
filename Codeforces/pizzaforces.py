#https://codeforces.com/problemset/problem/1555/A

n = int(input())
output_val = []
for i in range(n):
    people_no = int(input())
    if people_no % 8 == 0:
        output_val.append(int((people_no / 10) * 25))
    elif people_no % 7 == 0:
        output_val.append(int((people_no / 8) * 20))
    elif people_no % 6 == 0:
        output_val.append(int((people_no / 6) * 15))
    else:
        rem_10 = people_no % 10
        pizza_no = people_no // 10
        if rem_10 <= 6:
            output_val.append(pizza_no * 25 + 15)
        elif rem_10 <= 8:
            output_val.append(pizza_no * 25 + 20)
        else:
            output_val.append(pizza_no * 25 + 25)
for item in output_val:
    print(item)