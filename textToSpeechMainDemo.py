import speech_recognition as spTx #Speech to text
import pyttsx3 
import os
from gtts import gTTS as txSp #Text to speech



welcomeText = '(This is a demo!) Hi there! How may I help you?'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = txSp(text=welcomeText, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")

# Playing the converted file
os.system("start welcome.mp3")

# Python program to translate
# speech to text and text to speech

# Initialize the recognizer 
r = spTx.Recognizer() 

# Function to convert text to
# speech
def SpeakText(command):
    
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()
    
    
# Loop infinitely for user to
# speak

while(1):    
    
    # Exception handling to handle
    # exceptions at the runtime
    try:
        # use the microphone as source for input.
        with spTx.Microphone() as source1:
            
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source1, duration=0.2)
            
            #listens for the user's input 
            audio2 = r.listen(source1)
            
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            SpeakText(MyText)
            
    except spTx.RequestError as e:
        print(e)
        
    except spTx.UnknownValueError:
        print(spTx.UnknownValueError)