import pyttsx3  # Text-to-speeach converter library
import datetime  # Libraries to deal with date and time
import speech_recognition as sr # Library for performing speech recognition https://pypi.org/project/SpeechRecognition/
import wikipedia    # In order to extract data from Wikipedia,  Python Wikipedia library is used, which wraps the official Wikipedia API
import webbrowser   # The webbrowser module can be used to launch a browser in a platform-independent manner
import os        # The OS module in Python provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc.
import smtplib  # The smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon
import random   # For generating any random number

# The below code is to set the webBrowser
# If this piece of code is deleted then the program will automatically open in default web browser
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
webbrowser = webbrowser.get('chrome')

engine = pyttsx3.init("sapi5") # The pyttsx3 module supports two voices first is female and the second is male which is provided by “sapi5” for windows.
# sapi5 – SAPI5 on Windows
# nsss – NSSpeechSynthesizer on Mac OS X
# espeak – eSpeak on every other platform
voices = engine.getProperty("voices")   # Get all the voices from the system
# print(voices[1].id)
engine.setProperty("voice",voices[0].id)    # Set a particular voice for the engine

# Define a function which will call the engine to speak the parameter passed and then run and wait
def speak(audio):

    engine.say(audio)   
    # The runAndWait Gets if the engine is currently busy speaking an utterance or not. ... True if speaking, false if not. runAndWait () → None. Blocks while processing all currently queued commands.
    engine.runAndWait() # This function will make the speech audible in the system, if you don't write this command then the speech will not be audible to you.

# This function greets when the program is run
def wishMe():

    hour = int(datetime.datetime.now().hour)  # Getting the hour from the date time library
    if hour>=12 and hour<18:
        speak("Good Afternoon, sir")    
    elif hour<12 and hour>=0:
        speak("Good Morning, sir")
    else:
        speak("Good Evening, sir")

    speak("I am brainiac. How may i help you.")

# This function takes microphone input from the user and returns string output
def takeCommand():
    
    r = sr.Recognizer()  # This Speech recoganizer enables for a machine or program to identify words spoken aloud and convert them into readable text.
    with sr.Microphone() as source:  #pyAudio needs to be installed
        r.adjust_for_ambient_noise(source,duration=1) # This func is defined under the class Recoganiser of the speech recognisition
        # The ``duration`` parameter is the maximum number of seconds that it will dynamically adjust the threshold for before returning.
        print("Listening...")
        r.pause_threshold = 1   # seconds of non-speaking audio before a phrase is considered complete
        # r.energy_threshold = 500  this is if there is more noise in surrounding then you dont want them to be listened.
        audio = r.listen(source)    ## This func is defined under the class Recoganiser of the speech recognisition

    try:
        print("Recoganizing...")
        # Here query is a string
        query = r.recognize_google(audio,language="en-in")  # Performs speech recognition on ``audio_data`` (an ``AudioData`` instance), using the Google Speech Recognition API.
        print(f"User said: {query}\n")  # This will print the query said by the user
        # speak(query)
    except Exception as e:
        # print(e)
        speak("Could not understand what you want me to do. could you please say that again.")
        return "None"
    return query

def sendEmail(to, content):
    # first allow less secure app in your gmail account from which you are sending mail
    
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()  
    # Extended HELO (EHLO) is an Extended Simple Mail Transfer Protocol (ESMTP) command sent by an email server to identify itself when connecting to another email server to start the process of sending an email

    server.starttls()
    # STARTTLS is an email protocol command that tells an email server that an email client, including an email client running in a web browser, wants to turn an existing insecure connection into a secure one.

    # It will login to the email given
    server.login("manavsharma1208@gmail.com","Your-password")

    # here is the email of the sender
    server.sendmail("manavsharma1208@gmail.com",to,content)
    server.close()
    
if __name__ == "__main__":
    wishMe()
    while True:
        
        query = takeCommand().lower() # Takecommand will covenrt the speaked sentence into string
        #logic for executing tasks based on query

        if "hello" in query:
            speak("hi sir")
        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia..")
            print(results)
            speak(results)

        elif "open youtube" in query:
            speak("sure sir, Opening youtube")
            webbrowser.open("youtube.com") # This will open youtube using the webbrowser library in the browser specified

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

        elif "play music" in query:
            speak("here is the song for you...sir")
            music_dir="C:\\Users\\manav\\OneDrive\\Desktop\\my music"  #Specifing the directory address in which musics are kept
            songs = os.listdir(music_dir)    # This command will list all the music from the music directory provided
            #Further Use a loop to generate a random song
            # print(songs)
            rand_song=random.randint(0,len(songs)-1)    # This willcreate a random songs number from all the songs
            os.startfile(os.path.join(music_dir,songs[rand_song]))     # This command will first join the path of music dir to the path od os and then start that file 

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") # This will fetch the current time from datetime library
            speak(f"Sir, the time is {strTime}")    # It will speak the current time

        elif "open code" in query:
            codePath = "E:\\Microsoft VS Code\\Code.exe"       # Specifying the path of vscode
            os.startfile(codePath)  
        elif "email to manav" in query:
            #make a dictonary with key=name and value=emailid
            try:
                speak("what should i say")
                content = takeCommand()     # It will take the spoke command by user and return an string of that using google sppech_recognition library
                to = "gopal.1@iitj.ac.in"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir there was a problem while sending the email.")
                
                #speak("Do you want me to retry")
                # ans = takeCommand()
                # make a while loop and if the ans="no" then break the loop
        elif "quit" in query:
            speak("Ok sir...,have a nice day.....,shutting down")
            exit()


