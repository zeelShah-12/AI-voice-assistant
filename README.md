🔊 AI Voice Assistant
An AI-powered voice assistant built using Python that can respond to user commands and perform everyday tasks like opening websites, chatting, and responding to casual phrases.

🚀 Features
🎙️ Voice recognition using your microphone

🗣️ Text-to-speech responses

💬 Handles daily conversation phrases like:

“Hello”

“How are you?”

“Tell me something good”

“I'm sad”

“What’s up?”

🌐 Opens websites on command:

YouTube

LinkedIn

Pinterest

Google Calendar

📆 Can respond to simple greetings and motivational phrases

🛠️ Tech Stack
Python 3.x

speech_recognition

pyttsx3

webbrowser

flask (for web integration, optional)

🖥️ How to Run (Locally on VS Code)
Clone the Repository

bash
Copy
Edit
git clone https://github.com/zeelShah-12/ai-voice-assistant.git
cd ai-voice-assistant
Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the Assistant

bash
Copy
Edit
python app.py
Speak into your mic and watch it respond or open websites!

🗨️ Example Commands
Command	Response / Action
"Hello"	"Hi there!"
"How are you?"	"I'm good, how can I assist you?"
"I'm sad"	"I'm here for you. You're not alone."
"Tell me something good"	"Every day is a new beginning."
"Open YouTube"	Opens YouTube
"Open LinkedIn"	Opens LinkedIn
"Open Pinterest"	Opens Pinterest
"Open Calendar"	Opens Google Calendar

📁 File Structure
cpp
Copy
Edit
ai-voice-assistant/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    └── (optional images or icons)
📌 Notes
Works best in a quiet environment with a good microphone.

You can expand this by integrating with APIs like OpenAI, weather updates, or custom automation.
