"""Ask the user what their name is and how old they are."""

#ask the user for their name and say hello to them
name = input("What is your name? ")
print(f"Hello {name}.")

#ask the user for their age and double it
try:
    age = int(input("How old are you? "))
    age *= 2
    print(age)
except ValueError:
    #in case the age is not valid
    print("Enter a valid age")
    age = int(input("How old are you? "))

