# test_video_agent.py

import json
import os
from video_agent_wrapper import VideoAgent


def main():
    # Path to your lecture video
    video_path = "C:\\DDrive\\Projects\\GitHubRepository\\ai-lecture-system\\data\\input\\lecture.mp4"

    audio_path = "C:\\DDrive\\Projects\\GitHubRepository\\ai-lecture-system\\data\\audio\\audio.wav"
    import os

    print(os.environ["PATH"])
  # ✅ Step 0: Validate input path
    if not video_path or not os.path.exists(video_path):
        print(f"ERROR: Video file not found -> {video_path}")
        return {
            "status": "error",
            "message": "Invalid video path"
        }
    else:
        print(f"Valid video file found -> {video_path}")
    
    # Initialize Video Agent
    agent = VideoAgent(model_size="base")

    # Run agent
    output = agent.run(video_path, audio_path)

    # Pretty print result
    print("\n================ VIDEO AGENT OUTPUT ================\n")
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()