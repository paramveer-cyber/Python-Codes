import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
from selenium.webdriver.common.keys import Keys
import os
import smtplib
from PIL import Image,ImageGrab
import time
import psutil
import selenium
from selenium import webdriver
from googlesearch import search

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
path = "D:\\Applications\\chromedriver.exe"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeScreenshot():
    image = ImageGrab.grab()
    image.show()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! Sir hope your day goes well!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you ")

def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

battery = psutil.sensors_battery()
bat = battery.percent

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)


    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-hi')
        print(f"User said: {query}\n")

    except:
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()

while True:
    
    query = takeCommand().lower()
    
    if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

    elif 'open youtube' in query:
           webbrowser.open("https://www.youtube.com/")

    elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")

    elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
    elif 'open liked videos' in query:
            webbrowser.open_new("https://www.youtube.com/playlist?list=LL")
            
    elif 'open Dino game' in query:
            webbrowser.open("chrome://dino/")

    elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
    elif 'how are you' in query:
            speak('I am fine sir thank you')
            
    elif 'hi' in query:
            speak('hi sir how are you')
            
    elif 'mental' in query:
            speak('you are stupid')

    elif 'open your code' in query:
            speak('yes sir here it is')
            codePath = "D:\\PythonCodes\\Jarvis.py"
            os.startfile(codePath)
            
    elif 'screenshot' in query:
            speak('yes sir screen shot in 3 seconds  3                                ...2                                ...1')
            takeScreenshot()
    
    elif "open ms teams" in query:
            speak("yes Sir here it is")
            codePath = "C:\\Users\\PARAM\\AppData\\Local\\Microsoft\\Teams\\Update.exe" 
            os.startfile(codePath)

    elif 'battery' in query:
        if battery.power_plugged == False:
            speak(bat)
            speak("%               . . . and not plugged in")

        elif battery.power_plugged == True:
            speak(bat)
            speak("%                . . . and plugged in")

        else:
            speak('I dont know that')
            
    elif 'open chrome' in query:
            speak('yes sir here it is')
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
            
    elif 'open whatsapp' in query:
            speak('yes sir here it is')
            codePath = "C:\\Users\\PARAM\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(codePath)

    elif 'open minecraft' in query:
            speak('yes sir here it is')
            codePath = "C:\\Users\\PARAM\\AppData\\Roaming\\.minecraft\\TLauncher.exe"
            os.startfile(codePath)
            
    elif 'open arduino' in query:
            speak('yes sir here it is')
            codePath = "C:\\Program Files (x86)\\Arduino\\arduino.exe"
            os.startfile(codePath)

    elif 'stop' in query:
        speak("Ok Sir bye....")
        break

    elif 'google' in query:
        query_1 = query.replace("google ", "")
        for j in search(query_1, tld="com", num=1, stop=1, pause=1):
            print(j)
        driver = webdriver.Chrome(path)
        driver.get(j)

