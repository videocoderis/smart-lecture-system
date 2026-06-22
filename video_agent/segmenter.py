def build_segments(segments):
    structured = []

    for seg in segments:
        structured.append({
            "start": seg["start"],
            "end": seg["end"],
            "text": seg["text"]
        })

    return structured