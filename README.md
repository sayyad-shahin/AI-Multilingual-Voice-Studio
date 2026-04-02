# AI Multilingual Voice Studio

AI Multilingual Voice Studio is a full-stack web application that performs real-time text translation, Hinglish conversion, and text-to-speech audio generation. The application also includes an interactive harmonium feature that converts text into musical notes.

## Live Demo

Frontend: https://ai-multilingual-voice-studio.netlify.app  
Backend API: https://ai-multilingual-voice-studio.onrender.com

## Features

- Real-time multilingual translation  
- Hinglish (Hindi-English) output  
- Text-to-speech audio generation  
- Downloadable audio output  
- Voice input using speech recognition  
- Harmonium music notes from text  
- Simple and clean UI  

## Tech Stack

Frontend:
- HTML
- CSS
- JavaScript

Backend:
- Python
- Flask
- gTTS
- deep-translator

Deployment:
- Frontend: Netlify
- Backend: Render

## Project Structure

AI-Multilingual-Voice-Studio/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── audio_files/
│
├── frontend/
│   ├── index.html
│   └── sounds/
│
└── README.md

## How to Run Locally

Backend:

cd backend  
pip install -r requirements.txt  
python app.py  

Frontend:

Open frontend/index.html in browser

## API Endpoint

POST /process

Request:
{
  "text": "Hello world",
  "lang": "hi"
}

Response:
{
  "translated": "...",
  "hinglish": "...",
  "notes": ["sa", "re", "ga"],
  "audio_url": "..."
}

## Deployment

Backend is hosted on Render using Gunicorn  
Frontend is hosted on Netlify  

## Limitations

- Free hosting may be slow initially  
- Audio files are temporary  
- Limited usage on free plan  

## Author

Shahin Sayyad

## License

For educational and demo purposes
"# AI-Voice-Studio" 
