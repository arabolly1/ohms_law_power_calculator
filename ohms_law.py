print("=================================")
print("OHM'S LAW AND POWER CALCULATOR")
print("=================================")
# display the welcome message

print("WELCOME TO MY ENGINEERING PROJECT!")
print("THIS PROGRAM CALCULATE ELECTRICAL VALUES.")
# function to calculate voltage using ohms law

def calculate_voltage(current, resistance):
    voltage = current * resistance
    return voltage

print("\nSELECT A CALCULATION")
# repeat the calculator menu until the user exits
while True:
    print("1. calculate voltage")
    print("2. calculate current")
    print("3. calculate resistance")
    print("4. calculate power")
    print("5. Exit")
    # ask the user to select a calculation
    choice = input("enter your choice (1-5): ")
    if choice not in ["1", "2", "3", "4", "5"]:
        print("invalid choice! please select between 1 and 5.")
        continue
    if choice  == "5":
        print("thank you for using my calculator!")
        break
    
    print("you selected option;", choice)
    # calculate voltage using current multiplied by resistance
    if choice == "1":
        try:
            current = float(input("enter current in amperes: "))
        except ValueError:
            print("invalid input! please enter a number.")
            continue
        
        try:
            resistance = float(input("enter resistance in ohms: "))
        except ValueError:
            print("invalid input! please enter a number.")
            continue

        voltage = calculate_voltage(current, resistance)

        print("calculated voltage:", voltage, "volts")
        # calculate current usimg voltage divided by resistance
    elif choice == "2":
        try:
            voltage =float(input("enter voltage in volts: "))
        except ValueError:
            print("invalid input! please enter a number.")
            continue
        try:
            resistance = float(input("enter resistance in ohms: "))
        except ValueError:
            print("invalid input! please enter a number.")
            continue
        if resistance == 0:
            print("Error! Resistance cannot be zero.")
        else:
            current = voltage / resistance
            print("calculated current:", current, "amperes")
            # calculate resistance using voltage divided by current
    elif choice == "3":
        try:
            voltage = float(input("enter voltage in volts: "))
        except ValueError:
            print("invalid input! please enter a number.")
            continue
        try:
            current = float(input("enter cureent in amperes: "))
        except ValueError:
            print("invalid input! please enter a number.")
            continue
            
        if current == 0:
            print("error! current cannot be zero.")
        else:
            resistance = voltage / current
            print("calculated resistance:", resistance, "ohms")
            # calculate electrical power and check for high power
    elif choice == "4":
        try:
            voltage = float(input("enter voltage in volts: "))
        except ValueError:
            print("invalid input! please enter a number.")
            continue
        try:
            current = float(input("enter current in amperes: "))
        except ValueError:
            print("invalid input! please enter a number.")
            continue

        power = voltage * current

        if power > 100:
            print("warning: high power detected!")
            
        print("calculated power:", power, "watts")