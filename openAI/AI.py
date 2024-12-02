import json
import os
import openai
import pathlib
import sys
from time import sleep
from modules import clearConsole

# Gets the root directory of the project
# Gets the dataFileFolder directory
# Gets the config for openAI
rootDir = pathlib.Path(__file__).parents[1]

with open(rootDir/"config.json", "r") as file:
    paths = json.load(file)
dataFiles = rootDir/paths["dataFileFolder"]
AIconfig = dataFiles/paths["AIconfig"]
universalInstruction = dataFiles/paths["universalInstruction"]

class CHATBOT:
    def __init__(self, instruction, userName):
        # Opens the AIconfig.json and universalInstruction.json
        # config is just AIconfig.json
        with open(AIconfig, "r") as file:
            config = json.load(file)
        with open(universalInstruction, "r") as file:
            uInstruction = json.load(file)

        # Encapsulates the passed arguments
        
        self.uInstruction = uInstruction
        self.instruction = instruction
        self.userName = userName
        self.model = config["model"]
        self.name = config["name"]
        self.characterCtx = config["characterContext"]
        self.instructions = (f"{self.uInstruction['Instruction']}. You play the character: {self.name}. Their details: {self.characterCtx}. Here is the user selected resource: {self.instruction}")
        # Initialize openAI
        openai.api_key = self.getAPIKey()
        self.client = self.createClient()
        self.assistant = self.createAssistant()
        self.thread = self.createThread()


    # The Class's own functions (These are private functions)
    # Gets API Key from environment 
    def getAPIKey(self):
        try:
            return(os.getenv("OPENAI_API_KEY"))
        except:
            print("Something went wrong getting the environment 'OPENAI_API_KEY' value")

    # Creates the client
    def createClient(self):
        try:
            return(openai.OpenAI())
        except:
            print("Something went wrong creating openAI client")
    
    # Creates assistant
    def createAssistant(self):
        try:
            assistant = self.client.beta.assistants.create(
                model = self.model,
                instructions = self.instructions,
                name = self.name)
            return(assistant)
        except Exception as e:
            print(f"Something went wrong creating the openAI assistant: {e}")
        
    def createThread(self):
        try:
            return(self.client.beta.threads.create())
        except:
            print("Something went wrong creating the thread")

    def createMessage(self, message):
        
        try: 
            message = self.client.beta.threads.messages.create(
                thread_id = self.thread.id,
                role = "user",
                content = message)
            return(message)
        except:
            print(f"Something went wrong sending the meassage: {message}")

    def createRun(self):
        try:
            run = self.client.beta.threads.runs.create(
                thread_id=self.thread.id,
                assistant_id=self.assistant.id
            )
            return(run)
        except:
            print("Something went wrong creating the run")

    def retrieveRun(self, run):
        try:
            latestRun = self.client.beta.threads.runs.retrieve(
                    thread_id=self.thread.id,
                    run_id=run.id
                )
            return(latestRun)
        except:
            print("Something went wrong retrieving the latest run")
    
    def printAIResponse(self):
        messages = self.client.beta.threads.messages.list(
                        thread_id = self.thread.id
                    )
        for message in messages.data:
            if message.role == "assistant":
                print(f"\n{self.name}: {message.content[0].text.value}")
                break

    def runBot(self):
        # Clears the console
        clearConsole.doClear()
        # Warns the user
        print(f"WARNING! YOU ARE ABOUT TO CONVERSE WITH A LLM")
        print("IF YOU NEED SERIOUS HELP, IT IS IMPORTANT TO GO SEE A PROFESSIONAL")
        print("TYPE \"exit\" TO GO BACK TO MENU")
        # Print Thread Info
        print(f"\nAssistant: {self.assistant.id}")
        print(f"Thread ID: {self.thread.id}\n")

        sleep(4)
        try:
            self.createMessage(f"Summarize: {self.instructions} and ask the user if they have question")
            self.createRun()
            sleep(5)
            self.printAIResponse()
        except Exception as e:
            print(f"An error occured: {e}")
        while True:
            userInput = input(f"{self.userName}: ")
            if(userInput.lower() == "exit"):
                break
            try:            
                newMessage = self.createMessage(userInput)
                run = self.createRun()
            except Exception as e:
                print(f"An Error has occured: {e}")

            while run.status in ["queued", "in_progress"]:
                run = self.retrieveRun(run)
                if(run.status == "completed"):
                    self.printAIResponse()
                    break
                else:
                    print(".", end="", flush=True)
            
            



if __name__ == "__main__":
    print(sys.argv[0] + " is a module, please run main.py to start the program")
