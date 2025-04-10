# Grade Analyzer
# Written By Lachlan Harris


def main():
    # Prompt for name input, four score inputs and if the lowest score should be dropped for the grade calculation
    sName = input("Name of person that we are calculationg grades for: ")
    iScore1 = input_score_value("Enter test score 1: ")
    iScore2 = input_score_value("Enter test score 2: ")
    iScore3 = input_score_value("Enter test score 3: ")
    iScore4 = input_score_value("Enter test score 4: ")
    sDropLowestScore = input("Do you wish to drop the lowest grade? Y or N:  ").upper()
    
    # Check the value entered for droping lowest score is Y or N.
    # If valid values are entered, run the calculations, else display an error and exit
    # User experience would be better if it was switched to a while loop to check for an accepted value rather than exiting
    if sDropLowestScore in ("Y","N"):
        fAverageScore = calculate_average_score(iScore1,iScore2,iScore3,iScore4,sDropLowestScore)
        sGrade = calculate_letter_grade(fAverageScore)
        print(f"{sName} has a test average of: {format(fAverageScore,'.1f')}")
        print(f"Letter grade for the test is: {sGrade}")
    
    else:
        print("Invalid Entry: Enter Y to drop lowest grade or N to average all grades")
        exit()

def input_score_value(sPromptMessage): 
    # Initialize the iScoreValue variable with a -1 value to set it up for the while loop for input and validation
    iScoreValue = -1 
    while iScoreValue < 0:
    
        # Try to convert the input to an integer and check the score is not negative
        try :  
            iScoreValue = int(input(sPromptMessage))
            if iScoreValue >=0:
                break
            else:
                # Provide instructions if negative value is entered
                print("Invalid Entry: Negative values not accepted")
        # Provide instructions if non numeric or decimal value entered
        except ValueError:
            print("Invalid Entry: Score must be a whole number")
    # Return the user input        
    return iScoreValue


def calculate_average_score(iInputScore1,iInputScore2,iInputScore3,iInputScore4,sDropLowest):
    # Take each score input and the score drop collection to calculate the average
    if sDropLowest=="Y":
        # If lowest score should be dropped, compare each value to the other 3
        # If it is the lowest calculate the average of the other 3 values and divide by 3 to find the average
        if iInputScore1 <= iInputScore2 and iInputScore1 <= iInputScore3 and iInputScore1 <= iInputScore4:
            fAverage = (iInputScore2 + iInputScore3 + iInputScore4) / 3
            
        elif iInputScore2 <= iInputScore1 and iInputScore2 <= iInputScore3 and iInputScore2 <= iInputScore4:
            fAverage = (iInputScore1 + iInputScore3 + iInputScore4) / 3
            
        elif iInputScore3 <= iInputScore1 and iInputScore3 <= iInputScore2 and iInputScore3 <= iInputScore4:
            fAverage = (iInputScore1 + iInputScore2 + iInputScore4) / 3
            
        elif iInputScore4 <= iInputScore1 and iInputScore4 <= iInputScore2 and iInputScore4 <= iInputScore3:
            fAverage = (iInputScore1 + iInputScore2 + iInputScore3) / 3

    # If the user elected not to drop the lowest score, calculate average using all scores and divide by 4
    elif sDropLowest =="N":
        fAverage = (iInputScore1 + iInputScore2 + iInputScore3 + iInputScore4) / 4
    
    return fAverage

def calculate_letter_grade(iScore):
    # Step down the low end of each grade score range to return the letter grade corresponding to the students score
    # where the averaged score value is greater than or equal to the lowest value of the letter grade.
    sGradeLetter = ""
    
    if iScore >= 97.0:
        sGradeLetter = "A+"
    elif iScore >= 94.0:
        sGradeLetter = "A"
    elif iScore >= 90.0:
        sGradeLetter = "A-"
    elif iScore >= 87.0:
        sGradeLetter = "B+"
    elif iScore >= 84.0:
        sGradeLetter = "B"
    elif iScore >= 80.0:
        sGradeLetter = "B-"
    elif iScore >= 77.0:
        sGradeLetter = "C+"
    elif iScore >= 74.0:
        sGradeLetter = "C"
    elif iScore >= 70.0:
        sGradeLetter = "C-"
    elif iScore >= 67.0:
        sGradeLetter = "D+"
    elif iScore >= 64.0:
        sGradeLetter = "D"
    elif iScore >= 60.0:
        sGradeLetter = "D-"
    elif iScore < 60.0:
        sGradeLetter = "F"

    return sGradeLetter      
        
main()
