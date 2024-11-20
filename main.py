import json
import datetime
from modules import parseUserInput
from modules import menu
from modules import clearConsole
from openAI import AI


date = datetime.datetime.now()


# The name of the parser and the prefferedName of the user
parserName = "Apollo"
userName = input(f"{parserName}: Hello there beautiful stranger, who may I refer you as? ")

# Clears Console
clearConsole.doClear()

# Greets the user based on time
if(date.hour > 0 and date.hour < 12):
    print(f"{parserName}: Good morning, {userName}, and welcome! Here are the resources we can assist you with: ")
elif(date.hour >= 12 and date.hour <= 18):
    print(f"{parserName}: Good afternoon, {userName}, and welcome! Here are the resources we can assist you with: ")
else:
    print(f"{parserName}: Good evening, {userName}, and welcome! Here are the resources we can assist you with ")

choice = 0

# The main while loop that runs the program
while(choice != 5):
    try:
        print(f"{parserName}: Please choose one: ")
        menu.printMenu()
        choice = int(input(f"{userName}: "))
    except:
        print(f"{parserName}: Invalid choice. Please input a valid integer in the range (0 - 6).")
    
    match(choice):
        case 1:
            parseUserInput.parseInput(parserName,choice)
        case _:
            print(f"{parserName}: Not in the valid range, please try again")
