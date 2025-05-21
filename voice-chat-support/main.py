import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
import random
import datetime
import os
# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set voice properties
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

# Function for text-to-speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Setup speech recognizer
recognizer = sr.Recognizer()

# Function to listen for commands
def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  # Adjusts for ambient noise
        print("Listening for your command...")
        audio = recognizer.listen(source, timeout=10)  # Timeout after 10 seconds
    try:
        command = recognizer.recognize_google(audio)  # Google API to recognize speech
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return None
    except sr.RequestError:
        print("Sorry, I'm having trouble reaching the service.")
        return None
# Function to execute actions based on commands
def execute_command(command):
    command = command.lower()

    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    
    elif "play music" in command:
        webbrowser.open("https://open.spotify.com")
        speak("Opening Spotify and playing music")
    
    elif "what time is it" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
    
    elif "shutdown" in command:
        speak("Shutting down the computer")
        subprocess.Popen(["shutdown", "/s", "/t", "1"])
    
    elif "restart" in command:
        speak("Restarting the computer")
        subprocess.Popen(["shutdown", "/r", "/t", "1"])
    
    elif "tell me a joke" in command:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "I told my computer I needed a break, and now it won't stop sending me Kit-Kats.",
            "Why do programmers prefer dark mode? Because the light attracts bugs!"
        ]
        speak(random.choice(jokes))
    
    else:
        speak("Sorry, I don't understand that command.")
# Function to start listening for the wake word
def chat():
    while True:
        command = listen()
        if command:
            if "poplii" in command.lower():  # Listen for "Poplii"
                execute_command(command)
            else:
                speak("Please say 'Poplii' first to activate me.")
if __name__ == "__main__":
    chat()
