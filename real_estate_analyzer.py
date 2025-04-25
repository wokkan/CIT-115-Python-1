# Real Estate Analyzer
# By Lachlan Harris

def main():
    # Create a list and seed the user prompt variable we'll use to control the loop
    lSales = []
    sPromptForValue = "Y"
    
    # Loop to prompt the user to enter a sale value via a call to the getFloat which validates the entry. 
    # I also split the user prompt to enter another value into its own function to clean up the main function and make it consistent with the float input
    # Append the float value input to the list
    while sPromptForValue == "Y":
        fSalePrice = getFloatInput("Enter Sale price: ")
        sPromptForValue = getStringInput("Enter another value? Y OR N: ")
        
        lSales.append(fSalePrice)
     # Sort the sales list in preparation for processing
    lSales.sort()
    
    # After the sort, the first value [0] will be the lowest and the last [-1] will be the highest
    # Calculate the total of all values in the list using the built-in sum function, use the total divided by the list size (length) to calc the average 
    # Call the getMedian function with the sales list to calculate the median value
    fMinimumSale = lSales[0]
    fMaximumSale = lSales[-1]
    fTotalSales = sum(lSales)
    fMedianSale = getMedian(lSales)
    fAverageSale = fTotalSales / len(lSales)
    fCommission = fTotalSales * .03

    # Seed the property number for our loop to print each entered property value then loop through the list printing each with two decimal places with commas and alignment
    iPropertyCount = 1
    for fSale in lSales:
        print(f"{format('Property ','<10')}{iPropertyCount} $ {fSale: ,.2f}")
        iPropertyCount += 1
    # Print the calculated values, formatted to two decimal places with commas and alignment
    print(f"{format('Minimum:','<12')} $ {fMinimumSale: ,.2f}")
    print(f"{format('Maximum:','<12')} $ {fMaximumSale: ,.2f}")
    print(f"{format('Total:','<12')} $ {fTotalSales: ,.2f}")
    print(f"{format('Average:','<12')} $ {fAverageSale: ,.2f}")
    print(f"{format('Median:','<12')} $ {fMedianSale: ,.2f}")
    print(f"{format('Commission:','<12')} $ {fCommission: ,.2f}")


def getMedian(lSales):
    # The getMedian function takes the sales list, gets the list size (length) calculates the mid point by dividing by 2
    # If the list is even (size %2 = 0) then we take the precalculated midpoint, add it to the value before it (midpoint-1) and divide it by 2. 
    # Otherwise we just return the midpoint value
    fListSize = len(lSales)
    fMidPoint = int((fListSize / 2))
    if fListSize % 2 == 0:
        # List is even so we do the midpoint + (midpoint-1) calculation divided by 2
        
        fMedian = (lSales[fMidPoint] + lSales[fMidPoint - 1]) / 2
    else:
        # List isn't even so it must be odd, we can just set the value in our midpoint position as our median
        fMedian=lSales[fMidPoint]
    
    return fMedian

def getFloatInput(sPromptMessage): 
    
    while True:
    
        # Prompt for input, Try to convert the input to the specified datatype and check the input is above 0.
        # If the input is valid, return the value, otherwise show a message for a value below the minimum or invaid data type.
        
        try :  
            fInput = float(input(sPromptMessage))
            if fInput > 0:
                break
            else:
                # Provide instructions if the value entered is not greater than 0
                print("Invalid Entry: Please enter a value greater than 0")
        # Provide instructions if non numeric or invalid data type is entered
        except ValueError:
            print("Invalid Entry - Non-numeric value entered: Please enter a number greater than 0")
    # Return the user input     
       
    return fInput

def getStringInput(sPromptMessage): 
    # THis could have been placed in the main function but I like having the consistency of both user inputs being in their own functions
    # Start the loop, prompt the user for input, convert it to upper case for everyones sanity and check the value entered
    # If the user entered Y or N (or y or n) then exit the loop and return the value

    while True:
  
        sInput = input(sPromptMessage).upper()
        if sInput == "Y" or sInput == "N":
            
            break
  
    return sInput

main()