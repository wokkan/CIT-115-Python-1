# Compound Interest calculator
# Written by Lachlan Harris

# Prompt user to enter values for the interest calculation
# Decimals aren't expected for the componding frequency so we're using an integer there. All other fields may have decimals
fPrincipal = float(input("Enter the starting principal: "))
fInterest = float(input("Enter the annual interest rate: "))
iCompounding = int(input("How many times per year is the interest compounded? "))
fTerm = float(input("For how many years will the account earn interest? "))

# Calculate the future value of the investment.
fFutureValue = fPrincipal * (1+(fInterest / 100) / iCompounding) ** (iCompounding * fTerm)

# We're accepting float values for fTerm (years) to cover partial years 
# I didn't like how this printed when the user enters a whole number.
# To clean this up i'm using modulus and an if statement. 
# If the result of fTerm % 1 is 0 then it is a whole number and can be printed as an integer,
# otherwise the value is a float and can be expressed as such.  

print("At the end of", int(fTerm) if (fTerm % 1) == 0 else fTerm, "years you will have $",format(fFutureValue,',.2f'))


# I came up with an alternate option for fixing the year format by expressing fractions of a year as a mumber of months
# Using Modulus (%) and an if statement again, this time the if condition is multiplied by 12
# If (fTerm % 1) * 12 = 0 then a full year was entered and it can be printed as such
# If (fTerm % 1) * 12 > 0 then a decimal was entered, the result of the modulus will be used as the month value
# eg fTerm = 2.4:  2.4 % 1 = .3999;  .3999*12 = 4.7 ; 5 months (rounded to the nearest month)
# This would result in output of "2 years and 5 months"
# Leaving commented out as it probably goes beyond what is expected for formatting for this assignment but I had an itch to scratch...

#strTermText = str(int(fTerm // 1)) + " years and " + str(round((fTerm % 1)*12)) + " months" if (fTerm % 1)*12 > 0 else str(int(fTerm // 1)) + " years" 

#print("At the end of", strTermText, "you will have $",format(fFutureValue,',.2f'))

