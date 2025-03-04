import subprocess
import whisper
import os

# Specify paths
audio_file = "audio_files/recorded_audio.wav"  # Use the correct path to your audio file
ffmpeg_path = r"C:\ffmpeg\ffmpeg-7.1-essentials_build\ffmpeg-7.1-essentials_build\bin\ffmpeg.exe"  # Path to FFmpeg
output_file = "audio_files/recorded_audio.mp3"  # Temporary MP3 output file
transcription_file = "audio_files/recorded_audio_transcribed.txt"  # File to save transcription result

# Set the FFmpeg binary path for Whisper
os.environ["FFMPEG_BINARY"] = ffmpeg_path

# Convert audio file to MP3 using FFmpeg
subprocess.run([ffmpeg_path, "-i", audio_file, output_file])  # Use ffmpeg_path instead of just "ffmpeg"

# Load the Whisper model
model = whisper.load_model("base")
print("Loading Whisper model...")

def transcribe_audio():
    print("Transcribing audio...")
    # Now we use the MP3 file for transcription
    result = model.transcribe(output_file, fp16=False)  # Transcribe the audio
    print(f"Transcription: {result['text']}")  # Output transcription

    # Save transcription to a text file
    with open(transcription_file, 'w') as f:
        f.write(result['text'])

# Run the transcription function
transcribe_audio()
