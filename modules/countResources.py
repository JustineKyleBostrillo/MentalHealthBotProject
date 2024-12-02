import os
import sys
import json
import pathlib

rootDir = pathlib.Path(__file__).parents[1]

with open(rootDir/"config.json", "r") as file:
    config = json.load(file)
dataFiles = rootDir/config["dataFileFolder"]

dataFilesContent = os.listdir(dataFiles)

# Counts the number of json files that contains the substring "resource"
def countResourceFiles():
    dataFilesResourceCount = 0
    for i in range(len(dataFilesContent)):
        if("resource" in dataFilesContent[i]):
            dataFilesResourceCount += 1
    return dataFilesResourceCount

if __name__ == "__main__":
    print(sys.argv[0] + " is a module, please run main.py to start the program")
    