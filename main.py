import speech_recognition as sr

listener = sr.Recognizer()
try:
    global command
    with sr.Microphone() as source:
        print("listening...")
        voice= listener.listen(source)
        command = listener.recognize_google(voice)
        if 'babe' in command:
            command = command.replace('babe' , '')
            print(command)

except:
    pass 