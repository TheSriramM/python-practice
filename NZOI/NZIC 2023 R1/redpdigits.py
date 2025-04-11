#https://train.nzoi.org.nz/problems/1308

num = int(input())
rep_dig = []
num1 = "1"
num2 = "2"
num3 = "3"
num4 = "4"
num5 = "5"
num6 = "6"
num7 = "7"
num8 = "8"
num9 = "9"
count = 1
while int(num1) < num:
    num1 *= count
    rep_dig.append(num1)
    print(num1)
while int(num2) < num:
    count += 1
    num2 *= count
    rep_dig.append(num2)