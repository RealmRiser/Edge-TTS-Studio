from flask import Flask, render_template, request, jsonify
import edge_tts
import asyncio
import uuid
import os

import edge_tts.communicate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/voices')
def get_voices():
    async def fetch():
        voices = await edge_tts.list_voices()
        return sorted([v["ShortName"] for v in voices])
    return jsonify(asyncio.run(fetch()))

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.json
    text = data.get('text')
    voice = data.get('voice', 'en-US-JennyNeural')
    rate = data.get('rate', '+0%')
    pitch = data.get('pitch', '+0Hz')
    
    if not text:
        return jsonify({"status": "error", "message": "No text provided"}), 400

    filename = f"{uuid.uuid4().hex}.mp3"
    filepath = os.path.join('static', filename)
    
    async def gen():
        communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await communicate.save(filepath)
        
    asyncio.run(gen())
    return jsonify({"status": "success", "audio_url": f"/static/{filename}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
