import whisper

def transcribe_audio(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)

    return {
        "transcript": result["text"],
        "segments": result["segments"]
    }