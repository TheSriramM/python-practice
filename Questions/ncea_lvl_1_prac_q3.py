"""This program will track the amount the user spent starting from $200."""

amount = input("Enter the amount spent: ")
balance = 200
#list to store all the amounts that have been spent
leftover = []
while True:
    try:
        #checks if the input is valid
        amount = int(amount)
        balance -= amount
        if amount == 0:
            break
        elif balance <= 0:
            leftover.append(balance)
            break
        else:
            leftover.append(balance)
            amount = input("Enter the amount spent: ")
    except ValueError:
        #if the input isn't valid prints that's not a valid transaction
        print("That is not a valid transaction.")
        amount = input("Enter the amount spent: ")

print("My bank balances have been: ")
print("200")
for item in leftover:
    print(item)

