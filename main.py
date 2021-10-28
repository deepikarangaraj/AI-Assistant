import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import time

MASTER="Deepika"
engine = pyttsx3.init('sapi5')
engine.setProperty("rate", 150)
engine.setProperty("volume",0.7)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    print("Initializing D-five.....")
    
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning" + MASTER)
    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)
    speak("I am your desktop assistant How may I help you?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening...")
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        print("I'm sorry, I didn't catch what you said. Could you repeat it (more slowly)?")
        speak("I'm sorry, I didn't catch what you said. Could you repeat it (more slowly)?")
        query=None
    return query





    
wishme()


    #logic
while True:
    query=takecommand().lower()

    if "bye" in query:
            speak(f"Bye{MASTER} Take care")
            break

    elif "wikipedia" in query:
        speak("searching wikipedia")
        query = query.replace("wikipedia","")
        result = wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(result)
        speak(result)
        

    elif 'news' in query:
        news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
        speak('Here are some headlines from the Times of India,Happy reading')
        time.sleep(3)
        

    elif 'search'  in query:
        query = query.replace("search", "")
        webbrowser.open_new_tab(query)
        time.sleep(3)
        

    elif "open google" in query:
        speak("opening google")
        webbrowser.open_new_tab("https://www.google.com")
        time.sleep(5)
        

    elif "open youtube" in query:
        speak("opening youtube")
        webbrowser.open_new_tab("https://www.youtube.com")
        time.sleep(5)
        

    elif "open instagram" in query:
        speak("opening instagram")
        webbrowser.open_new_tab("https://www.instagram.com")
        time.sleep(5)
        

    elif "play music" in query:
        song_dir="C:\\Users\\New\\Music"
        song=os.listdir(song_dir)
        print(song)
        os.startfile(os.path.join(song_dir,song[1]))
        time.sleep(7)
        
        
    elif "time" in query:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {current_time}")
        

    elif "who are you" in query or "what can you do" in query:
        speak('I am D-Five your personal assistant. I am programmed to minor tasks like'
            'opening youtube,google chrome,and instagram  also predict time,,search wikipedia,play music' 
            ', and you can ask me jokes too!')
        
    
    elif "who made you" in query or "who created you" in query or "who discovered you" in query:
        speak("I was built by Deepika")
        print("I was built by Deepika")
        
    
    elif 'joke' in query:
        joke=pyjokes.get_joke()
        speak(joke)
        print(joke)
        

    elif "what's your name" in query:
        speak("I am D-Five. Your deskstop Assistant")
        

        

