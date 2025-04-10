# Assignment 2 Interplanetary weights
# Written by Lachlan Harris



# Set constants for each planets relative gravity
nMERCURY = 0.38
nVENUS   = 0.91
nMOON    = 0.165
nMARS    = 0.38
nJUPITER = 2.34
nSATURN  = 0.93
nURANUS  = 0.92
nNEPTUNE = 1.12
nPLUTO   = 0.066

# Prompt for Name and weight, set name string value in sName and weight float value in fWeight variable
sName = input("What is your name: ")
fWeight = float(input("What is your weight: "))

# Print calculated weight values for each planet with left aligned 20 wide names
# columns and right aligned 10 position columns with two decimal places.
# Planet weights are calculated using the formula (input weight) * (planet relative gravity)
print(f"{sName} here are your weights on our Solar System's planets:")
print( '{:20}'.format("Weight on Mercury:") + format(fWeight * nMERCURY,'>10,.2f'))
print( '{:20}'.format("Weight on Venus:") + format(fWeight * nVENUS,'>10,.2f'))
print( '{:20}'.format("Weight on Moon:") + format(fWeight * nMOON,'>10,.2f'))
print( '{:20}'.format("Weight on Mars:") + format(fWeight * nMARS,'>10,.2f'))
print( '{:20}'.format("Weight on Jupiter:") + format(fWeight * nJUPITER,'>10,.2f'))
print( '{:20}'.format("Weight on Saturn:") + format(fWeight * nSATURN,'>10,.2f'))
print( '{:20}'.format("Weight on Uranus:") + format(fWeight * nURANUS,'>10,.2f'))
print( '{:20}'.format("Weight on Neptune:") + format(fWeight * nNEPTUNE,'>10,.2f'))
# An alternate example of alignment and formatting using fstring
print(f"{format('Weight on Pluto:','<20')}{format(fWeight * nPLUTO,'>10,.2f')}")
