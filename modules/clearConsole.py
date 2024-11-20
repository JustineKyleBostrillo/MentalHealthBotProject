import os
import sys

# This simple module which clears the console of previous outputs
# If the OS is windows, do os.system('cls') if not, and for instance in linux, do os.system('clear')
def doClear():
    try:
        if(os.name == 'nt' or os.name == 'dos'):
            os.system('cls')
        else:
            os.system('clear')
    except:
        print("You're OS is not supported")

if __name__ == "__main__":
    print(sys.argv[0] + " is a module, please run main.py to start the program")