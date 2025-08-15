days, start, lowest = map(int, input().split())
money = list(map(int, input().split()))
done = False
finished = False

# for i in range(days):
#     if not done:
#         if money[i] <= lowest:
#             bought = start // money[i]
#             left = start - money[i] * bought
#             done = True
#             buy_money = money[i]
#             print(f"BUY {bought}")
#         else:
#             print("HOLD")
#     else:
#         if money[i] > buy_money:
#             if not finished:
#                 sold = money[i] * bought + left
#                 finished = True
#                 print(f"SELL {bought}")
#             else:
#                 print("WAIT")
#         else:
#             if finished:
#                 print("WAIT")
#             else:
#                 print("HOLD")

# print(sold - start)

for i in range(days):
    pass