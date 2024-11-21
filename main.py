import datetime
import json

from modules import parseUserInput
from modules import menu
from modules import clearConsole

from openAI import AI



date = datetime.datetime.now()


# The name of the parser, the AI, and the preferredName of the user
with open("config.json", "r") as file:
    config = json.load(file)
parserName = config["parserName"]
userName = input(f"{parserName}: Hey! I don't think we've met yet—I'm {parserName}! What's your name? ")

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
        print(f"{parserName}: Please select one: ")
        menu.printMenu()
        choice = int(input(f"{userName}: "))
    except:
        print(f"{parserName}: That's not a choice. Please put in a number between 0 and 5")
    
    match(choice):
        # If case is 0, 1, 2, 3, 4 
        case 0 | 1 | 2| 3 | 4:
            instruction = parseUserInput.parseInput(parserName,userName,choice)
            AI.CHATBOT(instruction, userName).runBot()
        case 5:
            print(f"{parserName}: Goodbye, {userName}, See you later!")
        case _:
            print(f"{parserName}: Not in the valid range, please try again")
