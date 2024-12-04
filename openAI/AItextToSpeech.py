import json
import os
import openai
import pathlib
import sys
from time import sleep
from modules import clearConsole
from modules import parseOpenAIKey

from gtts import gTTS as txSp #Text to speech


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
        self.language = paths["language"]
        self.uInstruction = uInstruction
        self.instruction = instruction
        self.userName = userName
        self.model = config["model"]
        self.name = "Friendly Chatbot"
        self.characterCtx = config["characterContext"]
        self.instructions = (f"{self.uInstruction['Instruction']}. Language: {self.language}. Here is the user selected resource: {self.instruction}")
        # Initialize openAI
        openai.api_key = self.getAPIKey()
        self.client = self.createClient()
        self.assistant = self.createAssistant()
        self.thread = self.createThread()


    # The Class's own functions (These are private functions)
    # Gets API Key 
    def getAPIKey(self):
        try:
            # return(os.getenv("OPENAI_API_KEY"))
            return(parseOpenAIKey.getAPIKey())
        except:
            print("Something went wrong getting openAI API Key")

    # Creates the client
    def createClient(self):
        try:
            return(openai.OpenAI())
        except Exception as e:
            print(f"Something went wrong creating openAI client. Maybe you put in the wrong key in 'config.json'. After editing, please restart your device and start again. ERROR: {e}" )
            exit(1)
    
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
            exit(1)
        
    def createThread(self):
        try:
            return(self.client.beta.threads.create())
        except Exception as e:
            print(f"Something went wrong creating the thread: {e}")
            exit(1)

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
    
    def outputAIResponse(self):
        messages = self.client.beta.threads.messages.list(
                        thread_id = self.thread.id
                    )
        for message in messages.data:
            if message.role == "assistant":
                print(f"\n{self.name}: {message.content[0].text.value}")
                message = txSp(text =  message.content[0].text.value, lang = self.language, slow = False)
                message.save("message.mp3")
                os.system("start message.mp3")

                break

    def runBot(self):
        # Clears the console
        clearConsole.doClear()
        # Warns the user
        print(f"WARNING! YOU ARE ABOUT TO CONVERSE WITH A LLM")
        print("IF YOU NEED SERIOUS HELP, IT IS IMPORTANT TO GO SEE A PROFESSIONAL")
        print("TYPE \"exit\" TO GO BACK TO MENU. WAIT (5s)")
        # Print Thread Info
        print(f"\nAssistant: {self.assistant.id}")
        print(f"Thread ID: {self.thread.id}\n")

        sleep(4)
        try:
            self.createMessage(f"Summarize: {self.instructions} and ask the user if they have question")
            self.createRun()
            sleep(5)
            self.outputAIResponse()
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
                    self.outputAIResponse()
                    break
                else:
                    print(".", end="", flush=True)
            
            



if __name__ == "__main__":
    print(sys.argv[0] + " is a module, please run main.py to start the program")
