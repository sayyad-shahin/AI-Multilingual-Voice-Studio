#  AI Multilingual Voice Studio

An AI-powered web application that converts text or speech into multiple languages with real-time translation, voice output, and interactive music generation.

---

##  Features

*  **Multilingual Translation**
  Translate text into multiple languages instantly

*  **Voice Input**
  Speak directly and convert speech to text

*  **Text-to-Speech (TTS)**
  Generate audio output for translated text

*  **Harmonium Music Generator**
  Converts text into musical notes and plays them

*  **Download Audio**
  Save translated speech as an MP3 file

---

##  Tech Stack

**Frontend:**

* HTML5
* CSS3 (Glass UI)
* JavaScript

**Backend:**

* Python (Flask)
* gTTS (Google Text-to-Speech)
* Deep Translator

---

##  Project Structure

```
AI-Multilingual-Voice-Studio/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── audio_files/
│
├── frontend/
│   └── index.html
│
└── README.md
```

---

##  Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/AI-Multilingual-Voice-Studio.git
cd AI-Multilingual-Voice-Studio/backend
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the backend server

```
python app.py
```

### 4. Open frontend

Open `index.html` in your browser

---

##  API Endpoint

### POST `/process`

**Request:**

```json
{
  "text": "Hello world",
  "lang": "hi"
}
```

**Response:**

```json
{
  "translated": "नमस्ते दुनिया",
  "notes": ["sa", "re", "ga"],
  "audio_url": "http://127.0.0.1:5000/audio/file.mp3"
}
```

---

##  Use Cases

* Language learning
* Voice-based translation tools
* AI-powered communication apps
* Educational music + speech experiments

---

##  Deployment

* Frontend: Netlify / Vercel
* Backend: Render / Railway

---

##  Future Improvements

* Add real AI voice (OpenAI / ElevenLabs)
* Improve UI animations
* Add more musical instruments
* Mobile responsive design

---

##  Author

Developed as an AI-powered full-stack project demonstrating real-time translation, speech synthesis, and interactive audio generation.

---

##  Show your support

If you like this project, give it a ⭐ on GitHub!
