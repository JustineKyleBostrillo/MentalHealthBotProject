import json
import openai
import pathlib
import sys

# Gets the root directory of the project

rootDir = pathlib.Path(__file__).parents[1]
dataFiles = rootDir/"dataFiles"

class CHATBOT:
    def __init__(self, config, instruction):
        print(2)

if __name__ == "__main__":
    print(sys.argv[0] + " is a module, please run main.py to start the program")
