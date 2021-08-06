import pyttsx3  # Text-to-speech converter library
import datetime  # Libraries to deal with date and time
# Library for performing speech recognition https://pypi.org/project/SpeechRecognition/
import speech_recognition as sr
import wikipedia    # In order to extract data from Wikipedia,  Python Wikipedia library is used, which wraps the official Wikipedia API
# The webbrowser module can be used to launch a browser in a platform-independent manner
import webbrowser
# The OS module in Python provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc.
import os
import smtplib  # The smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon
import random   # For generating any random number
import pywhatkit as pwk
import pyjokes

# The Google APIs Client Library for Python:
# pip install --upgrade google-api-python-client
# pip install --upgrade google-auth-oauthlib google-auth-httplib2


from pyaudio import PyAudio
import wave
from speech_recognition import AudioFile
from apiclient.discovery import build
from os import system

# The below code is to set the webBrowser
# If this piece of code is deleted then the program will automatically open in default web browser
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
webbrowser = webbrowser.get('chrome')

# The pyttsx3 module supports two voices first is female and the second is male which is provided by “sapi5” for windows.
engine = pyttsx3.init("sapi5")
# sapi5 – SAPI5 on Windows
# nsss – NSSpeechSynthesizer on Mac OS X
# espeak – eSpeak on every other platform
voices = engine.getProperty("voices")   # Get all the voices from the system
# print(voices[1].id)
# Set a particular voice for the engine
engine.setProperty("voice", voices[1].id)

# Define a function which will call the engine to speak the parameter passed and then run and wait


def speak(audio):

    engine.say(audio)
    # The runAndWait Gets if the engine is currently busy speaking an utterance or not. ... True if speaking, false if not. runAndWait () → None. Blocks while processing all currently queued commands.
    # This function will make the speech audible in the system, if you don't write this command then the speech will not be audible to you.
    engine.runAndWait()

# This function greets when the program is run


def wishMe():

    # Getting the hour from the date time library
    hour = int(datetime.datetime.now().hour)
    if hour >= 12 and hour < 18:
        speak("Good Afternoon Manab")
    elif hour < 12 and hour >= 0:
        speak("Good Morning Manab")
    else:
        speak("Good Evening Manab")

# This function takes microphone input from the user and returns string output


def takeCommand():

    # This Speech recoganizer enables for a machine or program to identify words spoken aloud and convert them into readable text.
    r = sr.Recognizer()
    with sr.Microphone() as source:  # pyAudio needs to be installed
        # This func is defined under the class Recoganiser of the speech recognisition
        r.adjust_for_ambient_noise(source, duration=1)
        # The ``duration`` parameter is the maximum number of seconds that it will dynamically adjust the threshold for before returning.
        print("Listening...")
        # seconds of non-speaking audio before a phrase is considered complete
        r.pause_threshold = 1
        # r.energy_threshold = 500  this is if there is more noise in surrounding then you dont want them to be listened.
        # This func is defined under the class Recoganiser of the speech recognisition
        audio = r.listen(source)

    try:
        print("Recoganizing...")
        # Here query is a string
        # Performs speech recognition on ``audio_data`` (an ``AudioData`` instance), using the Google Speech Recognition API.
        query = r.recognize_google(audio, language="en-in")
        # This will print the query said by the user
        print(f"User said: {query}\n")
        # speak(query)
    except Exception as e:
        # print(e)
        speak("Could not understand what you want me to do.")
        return "None"
    return query


def sendEmail(to, content):
    # first allow less secure app in your gmail account from which you are sending mail

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    # Extended HELO (EHLO) is an Extended Simple Mail Transfer Protocol (ESMTP) command sent by an email server to identify itself when connecting to another email server to start the process of sending an email

    server.starttls()
    # STARTTLS is an email protocol command that tells an email server that an email client, including an email client running in a web browser, wants to turn an existing insecure connection into a secure one.

    # It will login to the email given
    server.login("manavsharma1208@gmail.com", "Gopal13@")

    # here is the email of the sender
    server.sendmail("manavsharma1208@gmail.com", to, content)
    server.close()


def playOnYoutube(query):
    query = query.replace("on youtube", "")
    if "play" in query:
        query = query.replace("play", "")
    speak("playing"+query)
    pwk.playonyt(query)


if __name__ == "__main__":
    wishMe()
    while True:

        # Takecommand will covenrt the speaked sentence into string
        query = takeCommand().lower()
        # logic for executing tasks based on query

        if any(s in query for s in ("hi", "hello", "hey", "hay", "hai")):
            speak("hi sir, how are you")

        elif "your name" in query:
            speak("I am Ruby")

        elif "yourself" in query:
            speak(
                "Sure.. My name is Ruby. I am an AI assistant developed by Manab Gopal.")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia..")
            print(results)
            speak(results)

        elif "on youtube" in query:
            playOnYoutube(query)
            exit()

        elif "play music" in query:
            speak("here is the song for you...sir")
            # Specifing the directory address in which musics are kept
            music_dir = "C:\\Users\\manav\\OneDrive\\Desktop\\my music"
            # This command will list all the music from the music directory provided
            songs = os.listdir(music_dir)
            # Further Use a loop to generate a random song
            # print(songs)
            # This willcreate a random songs number from all the songs
            rand_song = random.randint(0, len(songs)-1)
            # This command will first join the path of music dir to the path od os and then start that file
            os.startfile(os.path.join(music_dir, songs[rand_song]))

        elif "whatsapp message" in query:
            try:
                speak("please provide a number to send messege")
                number = takeCommand()
                speak("what should i send?")
                messege = takeCommand()
                hour = int(datetime.datetime.now().hour)
                minute = int(datetime.datetime.now().minute)+2
                # added 2 extra minute to ensure that time does not change in between the process
                pwk.sendwhatmsg(f"+91{number}", messege, hour, minute, 8)
                speak("messege is send")
            except Exception as e:
                print(e)
                speak("Sorry could not send the messege")

        elif "search" in query:
            query = query.replace("search", "")
            if "on google" in query:
                query = query.replace("on google", "")
            pwk.search(query)
            exit()

        elif "play" in query:
            playOnYoutube(query)
            exit()

        elif "open youtube" in query:
            speak("sure sir, Opening youtube")
            # This will open youtube using the webbrowser library in the browser specified
            webbrowser.open("youtube.com")

        elif "open google" in query:
            speak("opening google")
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif "open facebook" in query:
            speak("ok sir,opening facebook")
            webbrowser.open("facebook.com")

        elif "open instagram" in query:
            speak("sure sir, opening instagram")
            webbrowser.open("instagram.com")

        elif "time" in query:
            # This will fetch the current time from datetime library
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            # It will speak the current time
            speak(f"Sir, the time is {strTime}")
            print("the time is - "+strTime)

        elif "joke" in query:
            My_joke = pyjokes.get_joke(language="en", category="neutral")
            print(My_joke)
            speak(My_joke)

        # elif "write" in query:
        #     speak("please say what should i write")
        #     writing = takeCommand()
        #     pwk.text_to_handwriting(writing,"C:\Users\manav\OneDrive\Desktop/test.png)

        elif "tell me" in query:
            query = query.replace("tell me", "")
            if "about" in query:
                query = query.replace("about", "")
            speak(f"sure sir, here is what i found about {query}")
            pwk.info(query)

        elif "open vs code" in query:
            codePath = "E:\\Microsoft VS Code\\Code.exe"       # Specifying the path of vscode
            os.startfile(codePath)

        elif "email to manav" in query:
            # make a dictonary with key=name and value=emailid
            try:
                speak("what should i say")
                # It will take the spoke command by user and return an string of that using google sppech_recognition library
                content = takeCommand()
                to = "gopal.1@iitj.ac.in"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir there was a problem while sending the email.")

                #speak("Do you want me to retry")
                # ans = takeCommand()
                # make a while loop and if the ans="no" then break the loop
        elif "shutdown" in query:
            speak("Ok sir...,have a nice day.....,shutting down")
            exit()
