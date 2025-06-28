from flask import Blueprint, request, jsonify, current_app
from vosk import Model, KaldiRecognizer
import wave
from pydub import AudioSegment
import io

recognition_bp = Blueprint('recognition', __name__)

# Load Vosk model once
try:
    model = Model("model/vosk-model-small-en-us-0.15")
    print("Vosk model loaded successfully")
except Exception as e:
    print(f"Failed to load Vosk model: {e}")
    model = None

@recognition_bp.route('/recognize', methods=['POST'])
def recognize():
    if model is None:
        return jsonify({'error': 'Speech recognition model not loaded'}), 500

    if 'file' not in request.files:
        return jsonify({'error': 'No audio uploaded'}), 400

    audio_file = request.files['file']

    try:
        # Convert MP3 to WAV mono 16-bit
        audio = AudioSegment.from_file(audio_file, format="mp3")
        audio = audio.set_channels(1).set_sample_width(2)
        wav_io = io.BytesIO()
        audio.export(wav_io, format="wav")
        wav_io.seek(0)

        wf = wave.open(wav_io, 'rb')

        rec = KaldiRecognizer(model, wf.getframerate())
        results = []

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                results.append(rec.Result())

        final_result = rec.FinalResult()
        results.append(final_result)

        return jsonify({'text': final_result})

    except Exception as e:
        current_app.logger.error(f"Recognition error: {e}")
        return jsonify({'error': 'Failed to process audio'}), 500
