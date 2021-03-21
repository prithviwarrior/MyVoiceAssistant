import speech_recognition as sr
import pyttsx3
import webbrowser as wb


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
                #speak(command)
    except:
        pass 
    return command

def run_babe():
    command = take_command()
    print(command)

    if 'how are you doing' in command:
        txt = "I'm doing great, thanks for asking. Anything I can help you with"
        speak(txt)
        print(txt)
    elif 'how are you' in command:
        txt = "Wonderful, thanks. What can I do for you?"
        speak(txt)
        print(txt)
    elif 'morning' in command:
        txt = "Very good morning, How may I help you?"
        speak(txt)
        print(txt)
    elif 'night' in command:
        txt = "Good night, Let me know if i have to set an alarm for you"
        speak(txt)
        print(txt)

while(True):
    run_babe()