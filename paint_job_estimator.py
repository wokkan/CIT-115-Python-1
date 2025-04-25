# Paint Job Estimator
# By Lachlan Harris

import math

def main():
    # Call the getFloatInput function with the input text as the argument and assign returned values to variables.
    # Convert entered state to upper case to simplify sales tax matching
    fWallArea=getFloatInput("Enter wall space in square feet: ")
    fPaintPrice=getFloatInput("Enter paint price per gallon: ")
    fPaintCoverage=getFloatInput("Enter Feet covered per gallon of paint: ")
    fLaborHoursPerGallon=getFloatInput("Enter hours of labor per gallon of paint: ")
    fLaborRate=getFloatInput("Enter labor charge per hour: ")
    sState = input("Enter first two letters of the state: ").upper()
    sCustomerName = input("Enter Customer Name: ")
    
    # Call the calculation functions with the entered values and\or calculated values returned from other functions 
    iTotalGallons = getGallonsOfPaint(fWallArea, fPaintCoverage)
    fLaborHours = getLaborHours(fLaborHoursPerGallon, iTotalGallons)
    fLaborCost = getLaborCost(fLaborHours, fLaborRate)
    fPaintCost = getPaintCost(iTotalGallons, fPaintPrice)
    fSalesTax = getSalesTax(sState)
    fTotalTax, fTotalCost = getTotals(fLaborCost, fPaintCost, fSalesTax)
    
    #Output the calculated results to the terminal and file
    showCostEstimate(iTotalGallons, fLaborHours, fLaborCost, fPaintCost, fTotalTax, fTotalCost, sCustomerName)
    

def getGallonsOfPaint(fWallArea, fPaintCoverage):
    # Receive the wall area and paint coverage per gallon to calculate the total gallons required, rounded to the next highest integer
    iGallons = math.ceil((fWallArea / fPaintCoverage))
    
    return iGallons

def getLaborHours(fLaborHoursPerGallon, iTotalGallons):
    # Receive the labor hours per gallon and total gallons required to calculate the total labor hours needed
    fLaborHours = iTotalGallons * fLaborHoursPerGallon

    return fLaborHours

def getLaborCost(fLaborHours,fLaborRate):
    # Receive the labor hours and the hourly labor rate to calculate the total labor cost
    fLaborCost= fLaborHours * fLaborRate
    
    return fLaborCost

def getPaintCost(iTotalGallons, fPaintPrice):
    # Receive the total gallons and price per gallon and calculate the total paint cost.
    fPaintCost = iTotalGallons * fPaintPrice
    return fPaintCost

def getSalesTax(sState):
    # Receive the state entered by the user. Step through the if\elif to return the tax rate if state entered matches an entry in the list.
    if sState == "CT":
        fTaxRate = .06
    elif sState == "MA":
        fTaxRate= .0625
    elif sState == "ME":
        fTaxRate = .085
        # This one wasn't really needed as it's essentially the same as our final else, but it was in the list so in it goes...
    elif sState == "NH":
        fTaxRate = .0
    elif sState == "RI":
        fTaxRate = .07
    elif sState == "VT":
        fTaxRate = .06
    else:
        fTaxRate = 0
    
    return float(fTaxRate)

def getTotals(fLaborCost, fPaintCost, fSalesTax):
    # Calculate the tax paid, rounded to 2 places and total cost also rounded to two places 
    # returns two values - tax and total cost
    fTotalTax = round((fLaborCost + fPaintCost) * fSalesTax,2)
    fTotalCost = round(fLaborCost + fPaintCost + fTotalTax,2)
    return fTotalTax, fTotalCost
#
def showCostEstimate(iTotalGallons, fLaborHours, fLaborCost, fPaintCost, fTotalTax, fTotalCost, sCustomerName):
    # Receive all the calculated values, along with the entered customer name
   
    # Print the formatted values to the terminal
    print(f"Gallons of Paint: {iTotalGallons}") 
    print(f"Hours of Labor: {format(fLaborHours,',.1f')}")
    print(f"Paint Charge: ${format(fPaintCost,',.2f')}") 
    print(f"Labor Charge: ${format(fLaborCost,',.2f')}") 
    print(f"Tax Paid: ${format(fTotalTax,',.2f')}") 
    print(f"Total Cost: ${format(fTotalCost,',.2f')}") 

    # Construct the output file name, open the file for writing and write the formatted values to the file
    # Print the file name to the terminal
    sOutputFile = sCustomerName + '_PaintJobOutput.txt'
    outfile = open(sOutputFile, 'w')
    outfile.write(f"Gallons of Paint: {iTotalGallons}\n") 
    outfile.write(f"Hours of Labor: {format(fLaborHours,',.1f')}\n")
    outfile.write(f"Paint Charge: ${format(fPaintCost,',.2f')}\n") 
    outfile.write(f"Labor Charge: ${format(fLaborCost,',.2f')}\n") 
    outfile.write(f"Tax Paid: ${format(fTotalTax,',.2f')}\n") 
    outfile.write(f"Total Cost: ${format(fTotalCost,',.2f')}\n") 
    print(f"File: {sOutputFile} was created.")


def getFloatInput(sPromptMessage): 
    
    while True:
    
        # Prompt for input, Try to convert the input to the specified datatype and check the input is above the minimum value we are accepting for the variable.
        # If the input is valid, return the value, otherwise show a message for a value below the minimum or invaid data type.
        
        try :  
            fInput = float(input(sPromptMessage))
            if fInput > 0:
                break
            else:
                # Provide instructions if a value below the minimum accepted value is entered
                print("Invalid Entry: Please enter a value greater than 0")
        # Provide instructions if non numeric or invalid data type is entered
        except ValueError:
            print("Invalid Entry: Please enter a valid number")
    # Return the user input     
       
    return fInput



main()

