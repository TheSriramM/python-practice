"""This program will check the voltage of batteries until you input a number that's zero or smaller than zero."""
voltage = input("Enter your input: ")
#list to store the beeps and the boops
beep_list = []
boundary = 1.2
while True:
    try:
        if float(voltage) >= 0:
            if float(voltage) >= boundary:
                beep_list.append("Beep")
                voltage = input("Enter your input: ")
            elif 0 <= float(voltage) < boundary:
                beep_list.append("Boop")
                voltage = input("Enter your input: ")
        elif float(voltage) < 0:
            break
    except ValueError:
        try:
            if float(voltage) < 0:
                break
        except ValueError:
            #if the input isn't a valid number
            print("Not robot compliant!")
            voltage = input("Enter your input: ")


#prints each item in the beep and the boop list
for item in beep_list:
    print(item)
    