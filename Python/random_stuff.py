age = input("What is your age? ")
while age.isnumeric() == False:
    print("Enter a valid number")
    age = input("What is your age? ")
age = int(age)
