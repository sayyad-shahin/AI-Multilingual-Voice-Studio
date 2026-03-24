from flask import Flask, request, jsonify, send_file
from deep_translator import GoogleTranslator
from flask_cors import CORS
from gtts import gTTS
import os
import uuid

app = Flask(__name__)
CORS(app)

#  Convert text → harmonium notes
def text_to_notes(text):
    notes_map = ['sa','re','ga','ma','pa','dha','ni']
    return [notes_map[ord(c) % 7] for c in text]


#  MAIN API
@app.route("/process", methods=["POST"])
def process():
    data = request.json
    text = data.get("text", "")
    lang = data.get("lang", "en")

    if not text:
        return jsonify({"error": "Empty input"}), 400

    try:
        translated = GoogleTranslator(source='auto', target=lang).translate(text)
    except:
        translated = "Translation failed"

    #  Unique audio file (important for production)
    filename = f"audio_{uuid.uuid4().hex}.mp3"
    filepath = os.path.join("audio_files", filename)

    os.makedirs("audio_files", exist_ok=True)

    tts = gTTS(text=translated, lang=lang if lang != "zh-CN" else "zh-cn")
    tts.save(filepath)

    return jsonify({
    "translated": translated,
    "notes": text_to_notes(text),
    "audio_url": f"https://ai-multilingual-voice-studio.onrender.com/audio/{filename}"
})

#  Serve audio
@app.route("/audio/<filename>")
def get_audio(filename):
    return send_file(os.path.join("audio_files", filename), as_attachment=False)

if __name__ == "__main__":
    app.run(debug=True)
