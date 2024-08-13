import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import subprocess

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.8  # Reduced pause threshold
        audio = r.listen(source, timeout=0.5, phrase_time_limit=3)

    try:
        print('Recognizing...')
        start_time = time.time()
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query} (recognized in {time.time() - start_time} seconds)")
    except Exception as e:
        speak('Say that again please...')
        return "none"

    return query


# To wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak('Good morning')
    elif hour > 12 and hour < 18:
        speak('Good afternoon')
    else:
        speak('Good evening')
    speak('I am Cypher sir, please tell me how can I help you')


# To send email
def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("skzaidu596@gmail.com", "vamf csxy rfdg gojv")
        server.sendmail('skzaidu596@gmail.com', to, content)
        server.close()
    except Exception as e:
        speak("Unable to send the email.")
        print(e)


# Define WhatsApp contacts
whatsapp_contacts = {
    'shaikh': '+919511859672',
    'jarvis': '+919511859672',
    # Add more WhatsApp contacts as needed
}

# Define email contacts
email_contacts = {
    'shaikh': 'techbot67@gmail.com',
    'jarvis': 'shaikhhasiburrahman4@gmail.com',
    # Add more email contacts as needed
}

if __name__ == '__main__':
    wish()
    while True:
        query = takecommand().lower()

        if 'send message on whatsapp' in query:
            speak("Whom do you want to send the message to?")
            name = takecommand().lower().strip()

            if name in whatsapp_contacts:
                speak(f"What message do you want to send to {name}?")
                message = takecommand().lower()
                hour = int(datetime.datetime.now().hour)
                minute = int(datetime.datetime.now().minute) + 2
                kit.sendwhatmsg(whatsapp_contacts[name], message, hour, minute)
                speak(f"Sending message to {name}")
            else:
                speak(f"Sorry, I don't have a WhatsApp contact saved as {name}.")

        elif 'play songs on youtube' in query:
            speak("Which song would you like to play?")
            song_name = takecommand().lower()
            if song_name != "none":
                kit.playonyt(song_name)
                speak(f"Playing {song_name} on YouTube")
            else:
                speak("Sorry, I didn't catch the song name.")

        elif 'send mail' in query:
            speak("Whom do you want to send the email to?")
            recipient = takecommand().lower()

            if recipient in email_contacts:
                speak(f"What should I say to {recipient}?")
                content = takecommand().lower()
                to = email_contacts[recipient]
                sendEmail(to, content)
                speak(f"Email has been sent to {recipient}.")
            else:
                speak(f"Sorry, I don't have an email contact saved as {recipient}.")

        elif 'open google' in query:
            speak('What do you want to search on Google?')
            cm = takecommand().lower()
            webbrowser.open(f"https://www.google.com/search?q={cm}")
            speak(f'Searching for {cm} on Google')

        elif 'open camera' in query:
            speak('Opening camera...')
            cap = cv2.VideoCapture(0)
            while True:
                ret, frame = cap.read()
                cv2.imshow('Camera', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break


        elif 'open notepad' in query:
            speak('Opening Notepad...')
            subprocess.Popen('C:\\Windows\\system32\\notepad.exe')

        elif 'open vs code' in query:
            speak('Opening VS Code...')
            subprocess.Popen('C:\\Users\\skzai\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')

        elif 'open virtualbox' in query:
            speak('Opening virtual box...')
            subprocess.Popen('C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox')

        elif 'open dsa python files' in query:
            speak('Opening Files...')
            subprocess.Popen('D:\\my practice programs\\python\\DSA In Python')

        elif 'open cmd' in query:
            speak('Opening Command Prompt...')
            subprocess.Popen('C:\\Windows\\system32\\cmd')

        elif "your name" in query:
             name = "My name is Cypher."
             speak(name)

        elif "how old are you" in query or "what's your age" in query:
             age = "I am six months old."
             speak(age)

        elif "your creator name" in query:
             creator = "My creator's name is Sk Zaidu."
             speak(creator)

        elif "introduce yourself" in query or "introduce about yourself" in query:
              self_intro = "My name is Cypher. I was created by Sk Zaidu in 2024 for personal use. How may I assist you sir ?"
              speak(self_intro)

        elif "what time is it" in query:
              current_time = datetime.datetime.now().strftime("%I:%M %p")
              speak(f"The current time is {current_time}.")
# closing apps
        elif 'close notepad' in query:
              speak('ok sir, closing notepad')
              os.system('taskkill /f /im notepad.exe')

        elif 'close vs code' in query:
            speak('ok sir, closing vs code')
            os.system('taskkill /f /im Code.exe')

        elif 'close cmd' in query:
            speak('ok sir, closing cmd')
            os.system('taskkill /f /im cmd.exe')

        elif 'close file' in query:
            speak('ok sir, closing file')
            os.system('taskkill /f /im file')

        elif 'you can sleep now' in query:
              speak('Thanks for using me sir, have a good day')
              sys.exit()
                # part of camera
              cap.release()
              cv2.destroyAllWindows()
        speak('Sir, do you have any other tasks for me?')



