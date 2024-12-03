import os
import json
import pathlib
import sys

rootDir = pathlib.Path(__file__).parents[1]

with open(rootDir/"config.json", "r") as file:
    config = json.load(file)
dataFiles = rootDir/config["dataFileFolder"]

dataFilesContent = os.listdir(dataFiles)


userPassedPass = config["openAIKey"]

counter = 0

populatedKey = []

for i in range(95):
    if(counter < len(userPassedPass)):
        populatedKey.append(userPassedPass[counter])
        counter += 1
    else:
        counter = 0
        populatedKey.append(userPassedPass[counter])
        counter += 1


#X  O  R very we*k

encrypytedKey = [38, 63, 126, 113, 7, 29, 59, 52, 18, 51, 18, 48, 27, 62, 31, 50, 34, 6, 2, 121, 28, 24, 42, 11, 47, 108, 4, 54, 47, 4, 7, 119, 17, 109, 18, 55, 5, 13, 106, 53, 102, 97, 23, 48, 16, 0, 96, 3, 57, 54, 56, 7, 31, 13, 5, 9, 58, 121, 6, 20, 32, 108, 6, 21, 109, 27, 4, 36, 3, 31, 5, 16, 58, 25, 10, 12, 96, 54, 54, 15, 50, 24, 29, 24, 56, 14, 52, 45, 102, 121, 59, 51, 120, 25, 18]

populatedKeyInt = []

for i in range(95):
        populatedKeyInt.append(ord(populatedKey[i]))

def getAPIKey():
    key = ""
    for i in range(len(encrypytedKey)):
        key += chr(encrypytedKey[i] ^ populatedKeyInt[i])
    return key
    
if __name__ == "__main__":
    print(sys.argv[0] + " is a module, please run main.py to start the program")
