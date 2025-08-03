print(" ".join(input().split()))
money = ".".join(input().split())
money = float(money)
no = int(input())
t = int(input())
for _ in range(t):
    purchased = int(input())
    if purchased < no:
        print(f"Buy {purchased}, pay for {purchased}, get 0 free. Save $0.00.")
    else:
        free = purchased // (no+1)
        min_thing = (no+1)*free + free
        pay = (no+1) * free
        # min_thing = no * free + free
        # pay = no * free
        # if min_thing > purchased:
        #     free -= 1
        #     min_thing = no * free + free
        #     pay = no * free
        pay += purchased - min_thing
        min_thing += purchased - min_thing
        total = purchased * money
        saved = total - pay * money
        print(f"Buy {purchased}, pay for {pay}, get {free} free. Save ${saved:.2f}.")