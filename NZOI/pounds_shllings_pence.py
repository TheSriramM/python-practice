n = int(input())
sums = int(input())
for i in range(n):
    #splits each number into a list
    sum_list = [input().strip("#").split("-") for x in range(sums)]
    final_pounds = [int(mon[0]) for mon in list(sum_list)]
    shilling = [int(mon[1]) for mon in list(sum_list)]
    pence = [int(mon[2]) for mon in list(sum_list)]
    pounds = sum(final_pounds)
    final_shillings = sum(shilling)
    final_pence = sum(pence)
    final_shillings += final_pence // 12
    pounds += final_shillings // 20
    final_shillings -= (final_shillings // 20) * 20
    final_pence -= (final_pence // 12) * 12
    print(f"#{pounds}-{final_shillings}-{final_pence}")