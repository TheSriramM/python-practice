"""This program will take input temperatures for different porridges and output whether the porridge is just right, too hot, or too cold."""
temp = input("Enter the temperature: ")
#the list that the output values will be added to
temp_list = []
breaking_temp = -1
boundary_cold = 34
boundary_hot = 42
while True:
    try:
        #checks if the temperature is a number
        temp = int(temp)
        if temp == breaking_temp:
            break
        elif boundary_cold <= temp <= boundary_hot:
            temp_list.append("just right")
            temp = input("Enter the temperature: ")
        elif temp < boundary_cold:
            temp_list.append("too cold")
            temp = input("Enter the temperature: ")
        elif temp > boundary_hot:
            temp_list.append("too hot")
            temp = input("Enter the temperature: ")
    except ValueError:
        #if the temperature is not a number then prints invalid temperature
        print("Invalid temperature.")
        temp = input("Enter the temperature: ")

for item in temp_list:
    print(item)   
