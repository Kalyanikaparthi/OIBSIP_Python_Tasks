# 🗣️ Voice Assistant – OIBSIP Python Task 1

## 📌 Objective
To build a voice-activated assistant in Python that can recognize voice commands and perform tasks like greeting, telling time/date, and searching the web.

---

## 🔧 Tools & Libraries Used
- `speech_recognition` – To capture and convert voice to text
- `pyttsx3` – To convert text to speech (TTS)
- `pywhatkit` – For performing Google search
- `datetime` – To get current time and date
- Python 3.x

---

## 🚀 Features Implemented
- Greets the user
- Tells current time and date
- Performs Google searches using voice
- Listens continuously until stopped

---

## 🔄 How It Works
1. The assistant listens using the microphone.
2. It uses Google's Speech Recognition to convert voice to text.
3. Based on keywords like `time`, `date`, or `search`, it performs actions.
4. It continues to listen until the user says `stop`, `exit`, or `bye`.

---

## ✅ Outcome
The assistant is capable of understanding and responding to basic voice commands. It can be extended further with more actions like playing music, opening apps, or sending emails.

---

## ▶️ How to Run
```bash
pip install speechrecognition pyttsx3 pywhatkit
python voice_assistant.py

---

## linkdin post
https://www.linkedin.com/posts/kalyani-kalyani-7a20a4375_python-voiceassistant-oasisinfobyte-activity-7354865473408147456-Fsfs?utm_source