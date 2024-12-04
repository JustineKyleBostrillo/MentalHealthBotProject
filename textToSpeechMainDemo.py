import datetime
import json

from modules import parseUserInput
from modules import menu
from modules import clearConsole
from modules import countResources

from openAI import AItextToSpeech


date = datetime.datetime.now()


# The name of the parser, the AI, and the preferredName of the user
with open("config.json", "r") as file:
    config = json.load(file)
parserName = config["parserName"]
clearConsole.doClear()
userName = input(f"{parserName}: Hey! I don't think we've met yet, I'm {parserName}! What's your name? ")

# Clears Console
clearConsole.doClear()

# Greets the user based on time
if(date.hour > 4 and date.hour < 12):
    print(f"{parserName}: Good morning, {userName}, and welcome! Here are the resources we can assist you with: ")
elif(date.hour >= 12 and date.hour <= 18):
    print(f"{parserName}: Good afternoon, {userName}, and welcome! Here are the resources we can assist you with: ")
else:
    print(f"{parserName}: Good evening, {userName}, and welcome! Here are the resources we can assist you with ")

choice = 0

# Gets the number of resources
numOfResources = countResources.countResourceFiles()

# The main while loop that runs the program
while(choice != numOfResources):#Num of resources is also exit
    try:
        print(f"{parserName}: Please select one: ")
        menu.printMenu()
        choice = int(input(f"{userName}: "))
    except:
        print(f"{parserName}: That's not a choice. Please put in a number between 0 and 5")
    

    if(choice in range(numOfResources)):     
        instruction = parseUserInput.parseInput(parserName,userName,choice)
        AItextToSpeech.CHATBOT(instruction, userName).runBot()
    elif(choice == numOfResources):
        print(f"{parserName}: Goodbye, {userName}, See you later!")
    else:
        print(f"{parserName}: Not in the valid range, please try again")

