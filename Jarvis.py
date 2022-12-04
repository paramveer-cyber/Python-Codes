import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import pyautogui
import os
from PIL import ImageGrab
import psutil
import time

greeting_words = ["hello", "hi", "hey", "how are you?"]
stop_words = ["stop", "quit", "break the code"]
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
path = "D:\\Applications\\chromedriver.exe"
battery = psutil.sensors_battery()
bat = battery.percent

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

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=10, timeout=5)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")
    except:
        print("Couldn't recognise anything...")  
    return query

def restart():
    from win32gui import GetWindowText, GetForegroundWindow
    if "Visual Studio Code" in (GetWindowText(GetForegroundWindow())): 
        pyautogui.hotkey('ctrl', 'shift', '`')
        pyautogui.typewrite("& D:/Python/python.exe d:/Python-Codes/Jarvis.py")
        pyautogui.press('enter')
    else:
        pyautogui.hotkey('win', '3')
        time.sleep(0.25)
        pyautogui.hotkey('ctrl', 'shift', '`')
        pyautogui.typewrite("& D:/Python/python.exe d:/Python-Codes/Jarvis.py")
        pyautogui.press('enter')

wishMe()

while True:
    query = takeCommand().lower()
    
    if 'wikipedia' in query:
        try:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        except:
            speak("Couldn't find anything on wikipedia")

    elif 'open youtube' in query:
           webbrowser.open("https://www.youtube.com/")

    elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")

    elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            
    elif 'open liked videos' in query:
            webbrowser.open_new("https://www.youtube.com/playlist?list=LL")
            
    elif 'open dino game' in query:
            webbrowser.open("chrome://dino/")

    elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S %p")    
            speak(f"Sir, the time is {strTime}")
            
    elif 'mental' in query:
            speak('you are stupid')

    elif 'open your code' in query:
            speak('yes sir here it is')
            codePath = "D:\\PythonCodes\\Jarvis.py"
            os.startfile(codePath)
            
    elif 'screenshot' in query:
            speak('yes sir screen shot in 3 seconds  3                                ...2                                ...1')
            takeScreenshot()
    
    elif 'battery' in query:
        bat = str(bat)
        if battery.power_plugged == False:
            speak((bat+"%               . . . and not plugged in"))
        elif battery.power_plugged == True:
            speak((bat+"%                . . . and plugged in"))
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

    elif 'close tab' in query:
        pyautogui.hotkey('ctrl' , 'w')

    elif 'reopen tab' in query:
        pyautogui.hotkey('ctrl' , 'shift', 't')

    elif query in greeting_words:
        speak("Hello")

    elif query in stop_words:
        speak("Ok Sir bye")
        break

    elif "reboot" in query: 
        restart()
        break

















    