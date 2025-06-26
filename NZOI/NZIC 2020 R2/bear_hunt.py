t = int(input())
total = 0
for _ in range(t):
    total += int(input())
if total < 60:
    # if time is less than 1 horu
    if total == 1:
        print("It took 1 minute")
    else:
        print(f"It took {total} minutes")
elif total % 60 == 0:
    if total == 60:
        print("It took 1 hour")
    else:
        print(f"It took {total//60} hours")
else:
    mins = total - (total // 60)*60
    hours = total // 60
    if mins == 1:
        if hours == 1:
            print(f"It took {hours} hour and 1 minute")
        else:
            print(f"It took {hours} hours and 1 minute")
    else:
        if hours == 1:
            print(f"It took {hours} hour and {mins} minutes")
        else:
            print(f"It took {hours} hours and {mins} minutes")