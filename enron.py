import pyttsx3
#text-to-speeach converter library
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
 
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[1].id)
engine.setProperty("voice",voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''
    it greets when the program is run

    '''
    hour = int(datetime.datetime.now().hour)
    if hour>=12 and hour<18:
        speak("Good Afternoon, sir")
    elif hour<12 and hour>=0:
        speak("Good Morning, sir")
    else:
        speak("Good Evening, sir")

    speak("I am brainiac. Please tell me how may i help you.")

def takeCommand():
    '''
    it takes microphone input from the user and returns string output

    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening...")
        r.pause_threshold = 1
        # r.energy_threshold = 500  this is if there is more noise in surrounding then you dont want them to be listened.
        audio = r.listen(source)

    try:
        print("Recoganizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")
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
    server.starttls()
    server.login("manavsharma1208@gmail.com","Gopal13#")
    server.sendmail("manavsharma1208@gmail.com",to,content)
    server.close()
    
if __name__ == "__main__":
    wishMe()
    while True:
        
        query = takeCommand().lower() #takecommand will covenrt the speaked sentence into string
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

        elif "play music" in query:
            speak("here is the song for you...sir")
            music_dir="C:\\Users\\manav\\OneDrive\\Desktop\\my music"
            songs = os.listdir(music_dir)
            #Further Use a loop to generate a random song
            # print(songs)
            rand_song=random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[rand_song]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "open code" in query:
            codePath = "E:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif "email to manav" in query:
            #make a dictonary with key=name and value=emailid
            try:
                speak("what should i say")
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
        elif "quit" in query:
            speak("Ok sir...,have a nice day.....,shutting down")
            exit()


