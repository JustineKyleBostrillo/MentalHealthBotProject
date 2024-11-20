#Parse user input to determine the proper resources to use
# This will also minimize the amount of token needed for the instruction for the AI and makes it more simpler
import json
import pathlib
import sys


# Gets the root directory of the project as well as where all the json files are (In dataFiles directory)
rootDir = pathlib.Path(__file__).parents[1]

with open(rootDir/"config.json", "r") as file:
    config = json.load(file)
dataFiles = rootDir/config["dataFileFolder"]

parserName = "Julius"
userName = "Ungas"


def parseInput(parserName, choice):
    match choice:
        # 
        case 1:
            with open(dataFiles/"resource_1.json", "r") as file:
                resource = json.load(file)
            
            resourceName = resource['Name']
            print(f"{parserName}: Here are the services for the resource '{resourceName}'.")

            userServicechoice = -1
            while(userServicechoice > (len(resource["Services"]) - 1)  or (userServicechoice < 0)):
                try:
                    print(f"{parserName}: Please choose one: ")
                    printServices(resource)
                    userServicechoice = int(input(f"{userName}: "))
                except:
                    print(f"{parserName}: Invalid choice. Please input a valid integer in the range (0 - {resource['Services']}).")
            
            # Assigns these variables to the appropriate value based on the selected service by the user
            parsedServiceName = resource["Services"][userServicechoice]["service_name"]
            parsedDescription = resource["Services"][userServicechoice]["description"]
            parsedUtils = resource["Services"][userServicechoice]["utilization"]
            parsedLink = resource["Services"][userServicechoice]["link"]
            parsedNumber = resource["ContactNumber"]
            parsedEmail = resource["ContactEmail"]
            parsedOfficeHours = resource["OfficeHours"]
            parsedLocation = resource["CampusLocation"]

            # All parsed put into one String as an instruction for the AI
            parsedIntruction = f"Resource name: {resourceName}. User selected service from resource: {parsedServiceName}. Its description: {parsedDescription}. Utilized for: {parsedUtils}. Link: {parsedLink}. Number: {parsedNumber}. Email: {parsedEmail}. Hours: {parsedOfficeHours}. Location: {parsedLocation}"

            print("".join(char for char in parsedIntruction if char not in "(){}[]\'\"").replace("..","."))


def printServices(resource):
    for i in range(len(resource["Services"])):
        Servicename = resource["Services"][i]["service_name"]
        print(f"{i} : {Servicename}")

if __name__ == "__main__":
    parseInput(parserName, 1)
    print(sys.argv[0] + " is a module, please run main.py to start the program")
