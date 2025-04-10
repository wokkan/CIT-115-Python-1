# Compound Interest Calculator
# By Lachlan Harris


def main():
    # Prompt for inputs using the validate input function.
    # The function expects arguments for the input prompt shown to the user and the accepted minimum value (zero or positive) along with data type for the input
    # For the purpose of this interest calculation, we're likely dealing with whole months only (compounding monthly) so I'm converting the month to an integer.

    fDeposit = validate_input("What is the original deposit (positive value): ", "positive",float)
    fInterestRate = validate_input("What is the interest rate (positive value): ", "positive",float)
    iMonths = validate_input("What is the number of months (positive value whole numbers only): ", "positive",int)
    fGoal = validate_input("What is the goal amount (enter a positive value or 0 for no goal): ", "zero",float)

    # Converting the the input interest rate to a monthly interest rate. 
    # I could have done this directly on the initial input but decided to keep the original variable input
    fMonthlyInterestRate = (fInterestRate / 100) / 12 
    
    # Seed our running balance variable with the initial deposit amount
    # Then we run through a loop calling the interest calculation function until we reach the number of months entered by the user (offset by 1 to show an accurate month count)
    # The updated balance is returned after each loop and sent back to the function as an argument with the monthly interest rate
    
    fBalance = fDeposit
    for iCompoundMonth in range(1,iMonths+1):
        fBalance = calculate_interest(fBalance, fMonthlyInterestRate)
        print(f"Month: {format(iCompoundMonth,'>3')} Account Balance is: $ {format(fBalance,',.2f')}")

    # First we check that a goal value greater than 0 was entered
    # To calculate the number of months to reach the goal amount we seed a variable with an initial value of 0 and our running goal balance variable with the initial deposit amount
    # We run through the same interest calculation function loop used for the monthly interest calculation, progressing the month counter forward by 1 each time
    # until the calculated goal balance is not less than the goal entered by the user and print the results.

    if fGoal > 0:
        iGoalMonths = 0
        fGoalBalance = fDeposit
        while fGoalBalance < fGoal:
            fGoalBalance = calculate_interest(fGoalBalance, fMonthlyInterestRate)
            iGoalMonths = iGoalMonths + 1
        
        print (f"It will take: {iGoalMonths} months to reach the goal of $ {format(fGoal,',.2f')}")

# Simple interest calculation function. Since we were using the same formula more than once it was placed in a function for consistency

def calculate_interest(fPrincipal, fMonthlyInterestRate):
    fCompundedAmount = fPrincipal + (fPrincipal * fMonthlyInterestRate)
    return fCompundedAmount

# This function handles input validation for our user inputs. It displays the appropriate prompt, checks for numeric values and ensures
# values entered meet the minimum required values we accept for the variable.
# Arguments expected are the prompt message, minimum value (positive or zero) and the datatype to return (defaults to float)

def validate_input(sPromptMessage,sMinimumValue,tDataType=float): 
    
    while True:
    
        # Prompt for input, Try to convert the input to the specified datatype and check the input is above the minimum value we are accepting for the variable.
        # If the input is valid, return the value, otherwise show a message for a value below the minimum or invaid data type.
        
        try :  
            iInput = tDataType(input(sPromptMessage))
            if (sMinimumValue=="positive" and iInput > 0) or (sMinimumValue=="zero" and iInput >= 0):
                break
            else:
                # Provide instructions if a value below the minimum accepted value is entered
                print("Invalid Entry: Please enter a value", "greater" if (sMinimumValue=="positive") else "equal to or greater", "than zero")
        # Provide instructions if non numeric or invalid data type is entered
        except ValueError:
            print("Invalid Entry: Please enter a valid number")
    # Return the user input     
       
    return iInput

main()

