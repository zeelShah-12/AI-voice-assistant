import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import random

# Initialize recognizer and TTS engine
listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            print(f"User said: {command}")
            return command
    except Exception as e:
        print("Sorry, I didn't catch that.")
        return ""

def run_assistant():
    command = take_command()
    
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The time is {time}")
    elif 'open google' in command:
        talk("Opening Google")
        webbrowser.open('https://www.google.com')
    elif 'joke' in command:
        jokes = [
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "I told my wife she was drawing her eyebrows too high. She looked surprised.",
            "Why don’t scientists trust atoms? Because they make up everything!"
        ]
        talk(random.choice(jokes))
    else:
        talk("Sorry, I can't help with that right now.")

if __name__ == '__main__':
    talk("Hi, how can I help you?")
    while True:
        run_assistant()
