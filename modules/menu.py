import sys

# This prints the Main Menu
# The current range is 0 - 6
def printMenu():
    print("----------MAIN MENU----------")
    print("1: UTSA Counseling Service")
    print("2: UTSA Wellness 360")
    print("3: Program, Events & Training")
    print("4: Recovery Support")
    print("5: Close The Program")


if __name__ == "__main__":
    print(sys.argv[0] + " is a module, please run main.py to start the program")
