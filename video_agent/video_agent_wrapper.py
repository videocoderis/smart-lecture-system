from audio_extractor import extract_audio
from transcriber import transcribe_audio
from segmenter import build_segments

class VideoAgent:
    def __init__(self, model_size="base"):
        print("Loading Video Agent...")
      #  self.transcriber = WhisperTranscriber(model_size)

    def run(self, video_path, audio_path):
        print("Video Agent started...")

        # Step 1: Extract audio
        audio_path1 = extract_audio(video_path, audio_path)

        # Step 2: Transcribe
        transcript_data  = transcribe_audio(audio_path)

        transcript = transcript_data["transcript"]
        segments = transcript_data["segments"]

        # Step 3: Structure output
        structured_segments = build_segments(segments)

        # Step 4: Final agent output
        result = {
            "source_video": video_path,
            "transcript": transcript,
            "segments": structured_segments
        }

        print("Video Agent completed")

        return result


# Optional direct function wrapper (if you want functional style also)
def video_agent(video_path):
    agent = VideoAgent(model_size="base")
    return agent.run(video_path)