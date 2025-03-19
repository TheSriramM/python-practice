"""This program will ask for the user's name and age and tell them if they can vote in NZ.
It will also ask if you are a resident, to make sure you can vote in NZ."""

#asks for the users name
name = input("What is your name? ")
age = input("What is your age? ")
while not age.isnumeric():
    print("Enter a valid age")
    age = input("What is your age? ")
age = int(age)

#checks if you are old enough
if age < 18:
    print("You can't vote in NZ.")
else:
    resident = input("Are you a resident in NZ? (yes or no) ")
    resident = resident.lower()
    if resident == "yes":
        print("You can vote in NZ!")
    elif resident == "no":
        print("You can't vote in NZ.")
    else:
        while True:
            #checks if the resident input is a yes or a no
            if resident != "yes" and resident != "no":
                print("Invalid response")
                resident = input("Are you a resident in NZ? (yes or no) ")
                resident = resident.lower() 
            else:
                if resident == "yes":
                    print("You can vote in NZ!")
                    break
                elif resident == "no":
                    print("You can't vote in NZ.") 
                    break
    