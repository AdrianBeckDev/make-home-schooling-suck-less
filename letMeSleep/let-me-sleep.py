# For boring and useless lessons or lectures
# Makes a loud tone whenever your name is called 

import speech_recognition as sr
from playsound import playsound
import keyboard as kb


# Create Recognizer Class
speech = sr.Recognizer()

#Define Mic
mic = sr.Microphone(device_index=0)

# print Microphone 
print(sr.Microphone.list_microphone_names())

# Define your name 

NAME = "Adrian"


with mic as source:
    audio = speech.listen(source)


result = r.recognize_google(audio)


home-schooling-sucks = True

while home-schooling-sucks():

    for words in result:
    
        if words = NAME:
            playsound('bing.mp3')

        if kb.wait('X'):
            home-schooling-sucks = False
            
