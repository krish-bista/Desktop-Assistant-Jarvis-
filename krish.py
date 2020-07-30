"""
Author - Krish Bista
Date - June 30 2020
Purpose - A virtual desktop assistant
"""

# Module importing part
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import requests
from PIL import ImageGrab


# Below are the functions for jarvis


def speak(audio):
    """
    It makes the program to speak
    :param audio:
    :return:
    """
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    """
    It greets the user according to time
    """
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak('Good morning sir')

    elif hour >= 12:
        if hour < 17:
            speak('Good afternoon sir')
        else:
            speak('Good evening sir')
    speak('All Functions are working properly. Modules are set and we are ready to go.')


def take_command():
    """
    It takes the users input as voice
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
        r.pause_threshold = 0.5
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in').lower()
        print(f'User said : {query}\n')
    except Exception:
        print('PLease say that again')
        return 'none'
    return query


def send_email(to, content):
    """
    Function for sending email
    :param to:
    :param content:
    :return:
    """
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Your email id', 'Your password')
    server.sendmail('Your email id', to, content)
    server.close()


def weather():
    """
    IT tells the weather status temperature and other stuffs
    :return:
    """
    url = 'https://openweathermap.org/data/2.5/weather?q=Biratnagar,nepal&appid=439d4b804bc8187953eb36d2a8c26a02'
    response = requests.get(url)
    response_json = response.json()
    weather_status = response_json['weather'][0]['description']
    temperature = response_json['main']['temp']
    humidity = response_json['main']['humidity']
    wind_speed = response_json['wind']['speed']
    output = f'Current weather status is {weather_status}. Temperature is {temperature}. Humidity is {humidity} and ' \
             f'wind speed is {wind_speed} '
    return output


def take_screenshot():
    """
    It will take screenshot
    """
    image = ImageGrab.grab()    
    image.show()


if __name__ == '__main__':
    wish_me()
    while True:
        query = take_command().lower()
        # Logic for executing task based on query
        if 'wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak('According to Wikipedia')
                print(results)
                speak(results)

            except Exception:
                speak("Please try again !Sir")

        elif 'who are you' in query:
            speak("Sir, I am Jarvis created by Mr.Krish Besta on June 30 2020")

        elif "open youtube" in query:
            speak('Opening Youtube')
            webbrowser.open('www.youtube.com')

        elif "open google" in query:
            speak('Opening Google')
            webbrowser.open('google.com')

        elif "bye" in query:
            speak('Bye sir, thanks for your time')
            exit()

        elif "hello how are you" in query:
            speak('Hi sir, I am fine')

        elif "play music" in query:
            webbrowser.open('https://www.youtube.com/watch?v=gbWQVk9cVtE')

        elif "open 4k gaming" in query:
            webbrowser.open("https://www.youtube.com/channel/UCSslzCYfi-PA6q1atGYUqSg")

        elif "time" in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir, The time is {strTime}')

        elif 'zoom' in query:
            zoomPath = "C:\\Users\\admin\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(zoomPath)
        elif 'email' in query:
            dictOfEmails = {'akhil': 'akhiljha977@gmail.com', 'saurabh': 'tsaurabh007@gmail.com'}
            try:
                speak('To whom should I send ?')
                to = take_command().lower()
                if to in dictOfEmails.keys():
                    to = dictOfEmails[to]
                    speak('What should I say ?')
                    content = take_command()
                    send_email(to, content)
                    speak("Email sent")
                else:
                    speak("Email not found")
            except Exception:
                speak("I could not send the email")

        elif "weather" in query:
            speak(weather())
        
        elif "screenshot" in query:
            take_screenshot()
            speak("Screenshot taken")
    