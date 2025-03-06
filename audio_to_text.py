import whisper
import os

# Configuration
AUDIO_FILE = "audio_files/recorded_audio.wav"
TRANSCRIPT_DIR = "transcribed_audio"
TRANSCRIPT_FILE = os.path.join(TRANSCRIPT_DIR, "transcription.txt")

def transcribe_audio():
    if not os.path.exists(AUDIO_FILE):
        print(f"Error: {AUDIO_FILE} not found. Please record an audio file first.")
        return
    
    # Ensure the output directory exists
    os.makedirs(TRANSCRIPT_DIR, exist_ok=True)

    print("Loading Whisper model...")
    model = whisper.load_model("base")  # Use "tiny", "small", "medium", or "large" for different accuracy levels

    print("Transcribing audio...")
    result = model.transcribe(AUDIO_FILE)

    # Save the transcription
    with open(TRANSCRIPT_FILE, "w", encoding="utf-8") as f:
        f.write(result["text"])

    print(f"Transcription saved: {TRANSCRIPT_FILE}")
    print("\nTranscription Output:\n" + result["text"])

if __name__ == "__main__":
    transcribe_audio()
