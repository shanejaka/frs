import asyncio
import io
import os

from flask import Flask, request, send_file, render_template, jsonify

import edge_tts

import nest_asyncio
nest_asyncio.apply()

app = Flask(__name__)

# Voices available in the UI. Add more edge-tts Myanmar/English voices here if you want.
VOICES = {
    "my-MM-ThihaNeural": "Thiha (Male)",
    "my-MM-NilarNeural": "Nilar (Female)",
}


async def _synthesize(text: str, voice: str) -> bytes:
    """Generate speech audio bytes using edge-tts."""
    communicate = edge_tts.Communicate(text, voice)
    audio_data = bytearray()
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_data.extend(chunk["data"])
    return bytes(audio_data)


@app.route("/")
def index():
    return render_template("index.html", voices=VOICES)


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json(silent=True) or {}
    text = (data.get("text") or "").strip()
    voice = data.get("voice") or "my-MM-ThihaNeural"

    if not text:
        return jsonify({"error": "စာသားထည့်ပေးပါ (Please enter some text)"}), 400

    if voice not in VOICES:
        return jsonify({"error": "မမှန်ကန်သော အသံ (Invalid voice selected)"}), 400

    try:
       loop = asyncio.new_event_loop() 
       asyncio.set_event_loop(loop) 
       audio_bytes = loop.run_until_complete(_synthesize(text, voice)) 
       loop.close()
    except Exception as exc:
       
        import traceback
        traceback.print_exc() 
        return jsonify({"error": f"Error: {str(exc)}"}), 500

    if not audio_bytes:
        return jsonify({"error": "အသံဖိုင် မထုတ်နိုင်ပါ (No audio generated)"}), 500

    audio_buffer = io.BytesIO(audio_bytes)
    audio_buffer.seek(0)
    return send_file(
        audio_buffer,
        mimetype="audio/mpeg",
        as_attachment=False,
        download_name="myanmar_tts.mp3",
    )


if __name__ == "__main__":
    # Local dev only. On Render, gunicorn runs the app (see Procfile).
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
