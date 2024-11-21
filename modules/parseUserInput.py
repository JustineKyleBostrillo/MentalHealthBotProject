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


def parseInput(parserName, userName, choice):
    filePath = dataFiles/f"resource_{choice}.json"
    with open(filePath) as file:
        resource = json.load(file)
        userServicechoice = -1
        while(userServicechoice > (len(resource["Services"]) - 1) or (userServicechoice < 0)):
            try:
                print(f"{parserName}: Please choose one: ")
                printServices(resource)
                userServicechoice = int(input(f"{userName}: "))
            except:
                print(f"{parserName}: Invalid choice. Please input a valid integer in the range (0 - {len(resource['Services'])}).")
        # print(resource["Services"])
    rawInstruction = f"Resource Name: {resource['Name']}. Info about the resource: {resource['Info']}. Number: {resource['ContactNumber']}. Email: {resource['ContactEmail']}. When it is open: {resource['OfficeHours']}. Campus location: {resource['CampusLocation']}"
    for key, value in resource["Services"][userServicechoice].items():
        rawInstruction += (f"{key}: {value}. ")
    instruction = ''.join(c for c in rawInstruction if c not in "()[]\'\"").replace("..", ".")

    return(instruction)


def printServices(resource):
    for i in range(len(resource["Services"])):
        Servicename = resource["Services"][i]["service_name"]
        print(f"{i} : {Servicename}")

if __name__ == "__main__":
    print(sys.argv[0] + " is a module, please run main.py to start the program")
