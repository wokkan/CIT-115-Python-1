# Temperature Converter
# Written by Lachlan Harris


print("Welcome to Lachlan Harris's Temperature Converter")

# Prompt the user for a temperature value (float) and unit
fTemp = float(input("Enter a temperature: "))
sTempUnit = input("Is the temperature F for Farenheit or C for Celsius? ")

# Check the entered temperature unit
# We ask for an F or C, but I wont punish the user for incorrect case
if sTempUnit in ("f","F"):
    # If the user entered one of the accepted variations of Farenheit
    # We're going to check the temp value entered is equal to or less than 212
    # If so we'll run the calculation and output the result to 1 decimal place
    # Otherwise, the user will be informed the value exceeded the maximum accepted temp
    
    if fTemp <=212:
        print(f"The Celsius equivalent is: {round((5.0/9.0) * (fTemp - 32),1)}")
    else:
        print("Temp can not be > than 212F")

elif sTempUnit in ("c","C"):
    # if the user entered one of the accepted variations of Celsius
    # we're going to check the temp value entered is equal to or less than 100
    # If so, we'll run the calculation and output the result to 1 decimal place
    # Otherwise, the user will be informed the value exceeded the maximum accepted temp

    if fTemp <= 100:
        print(f"The Farenheit equivalent is: {round(((9.0/5.0) * fTemp) + 32,1)} ")
    else:
        print("Temp can not be > than 100C")
        
else:
    # If the user did not enter F or C, provide instruction.
    print("You must enter F or C")

