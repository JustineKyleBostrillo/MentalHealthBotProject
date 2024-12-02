import sys
import json
import pathlib
import os
# This prints the Main Menu
rootDir = pathlib.Path(__file__).parents[1]

with open(rootDir/"config.json", "r") as file:
    config = json.load(file)
dataFiles = rootDir/config["dataFileFolder"]

dataFilesContent = os.listdir(dataFiles)

#Gets the json files that contains the substring "resource"
def getResourceFiles():
    files = []
    for i in range(len(dataFilesContent)):
        if("resource" in dataFilesContent[i]):
            files.append(dataFilesContent[i])
    return files

def printMenu():
    resourceFiles = getResourceFiles()
    print("----------MAIN MENU----------")
    for i in range(len(resourceFiles)):
        filePath = dataFiles/f"resource_{i}.json"
        with open(filePath) as file:
            resource = json.load(file)
        print(f"{i}: {resource['Name']}")
    print(f"{len(resourceFiles)}: Exit")


if __name__ == "__main__":
    print(sys.argv[0] + " is a module, please run main.py to start the program")
