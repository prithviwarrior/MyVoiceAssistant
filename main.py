import speech_recognition as sr
import pyttsx3


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        global command
        with sr.Microphone() as source:
            print("listening...")
            voice= listener.listen(source)
            command = listener.recognize_google(voice)
            if 'babe' in command:
                command = command.replace('babe' , '')
                print(command)
                speak(command)
    except:
        pass 
    return command


take_command()