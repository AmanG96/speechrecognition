import os
import random
import time
import webbrowser
from time import ctime

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

rec = sr.Recognizer()

# Function to record the audio------------------------------------------------


def record_audio(ask=False):
    if ask:
        
        bot_speak(ask)
    with sr.Microphone() as source:
        audio = rec.listen(source)
        voice_data = ''
        try:
            voice_data = rec.recognize_google(audio)
        except sr.UnknownValueError:
            bot_speak("Sorry did not understand.")
        except sr.RequestError:
            bot_speak("Sorry the service is down at the moment.")
        return voice_data

# Function for the bot to speak-----------------------------------------------


def bot_speak(audio_string):
    tts = gTTS(text=audio_string, lang="en", slow=False)
    r = random.randint(1, 10000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


# Function to respond to the question-----------------------------------------
def respond(voice_data):

    # If name is asked
    if "what is your name" in voice_data:
        bot_speak("It can be whatever you want it to be!")

    # If time is asked
    if "what time is it" in voice_data:
        bot_speak(ctime())

    # if search is asked
    if "search" in voice_data:
        search = record_audio("What do you want to search for?")
        url = f"https://www.google.com/search?q={search}"
        bot_speak("Here is what I found")
        try:
            webbrowser.get('chromium').open(url)
        except webbrowser.Error:
            print("Can't open")

    # If location is asked
    if "find location" in voice_data:
        location = record_audio("What do you want to search for?")
        url = f"https://www.google.nl/maps/place/{location}/&amp"
        bot_speak("Here is what I found")
        webbrowser.get('chromium').open(url)

    # if asked to exit
    if "exit" in voice_data:
        bot_speak("Thank you, see you next time.")
        exit()


time.sleep(1)
while 1:
    bot_speak("How can I help you?")
    vc_data = record_audio()
    respond(vc_data)
