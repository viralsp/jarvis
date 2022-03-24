from email.mime import audio
from logging import exception
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
     hour = int(datetime.datetime.now().hour)
     if hour>0 and hour<12:
         speak("good morning!")
     elif hour>=12 and hour<18:
         speak("good afternoon!")
     else:
         speak("good evening!")

     speak("I am jarvis!. please let me know how can i help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.......")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said :{query}\n")

    except exception as e:
        #print(e)
        print("say that again please...")
        return "None"
    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password here')
    server.sendemail('youremail@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
   # speak("great")
    wish()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("https://stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\musics'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is{strTime}")

        elif 'quit' in query:
            exit()


        elif 'open pycharm' in query:
            pycharmPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.3\\bin\\pycharm64.exe"
            os.startfile(pycharmPath)

        elif 'send email' in query:
            try:
                speak("what should i say")
                content = takecommand()
                to = "youremail@gmail.com"
                sendEmail(to,content)
                speak("email has been sent")
            except Exception as e:
                speak("sorry!, i am unable to sent an email to you")