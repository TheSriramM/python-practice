#https://train.nzoi.org.nz/problems/1308

# num = int(input())
# rep_dig = []
# num1 = "1"
# num2 = "2"
# num3 = "3"
# num4 = "4"
# num5 = "5"
# num6 = "6"
# num7 = "7"
# num8 = "8"
# num9 = "9"
# count = 1
# while int(num1) < num:
#     num1 *= count
#     rep_dig.append(num1)
#     print(num1)
# while int(num2) < num:
#     count += 1
#     num2 *= count
#     rep_dig.append(num2)

# WTH is this!!!
# My new code for subtask 1
# Works!!!
num = int(input())
length = len(str(num))
elevenDiv = (num // 11)*11
output = []
if num - elevenDiv == 10:
    output.append(2)
    output.append(8)
    output.append(elevenDiv)
elif num - elevenDiv == 0:
    output.append(elevenDiv)
else:
    output.append(num - elevenDiv)
    output.append(elevenDiv)

print(len(output))
for item in output:
    print(item)