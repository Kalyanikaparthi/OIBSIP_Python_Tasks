import speech_recognition as sr
import pyttsx3
import pywhatkit 
import datetime

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    """Speak out the text."""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to the user's voice and convert it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        command = command.lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, I'm having trouble connecting to the service.")
        return ""

def run_assistant(command):
    """Process the given command."""
    if "hello" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}")

    elif "date" in command:
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today is {today}")

    elif "search for" in command:
        topic = command.replace("search for", "").strip()
        if topic:
            speak(f"Searching for {topic}")
            pywhatkit.search(topic)
        else:
            speak("What would you like me to search for?")

    else:
        speak("I didn't understand that command.")

# 🟢 Main loop with exit condition
speak("Voice Assistant is now running. Say 'stop' or 'exit' to quit.")

while True:
    command = listen()

    if any(quit_word in command for quit_word in ["stop", "exit", "bye"]):
        speak("Goodbye! Shutting down.")
        break

    if command:
        run_assistant(command)