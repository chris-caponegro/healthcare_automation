import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import keyboard
import os

# Configuration
SAMPLE_RATE = 44100  # Sample rate in Hz
CHANNELS = 1  # Mono audio
AUDIO_DIR = "audio_files"
AUDIO_FILE = os.path.join(AUDIO_DIR, "recorded_audio.wav")

# Ensure the directory exists
os.makedirs(AUDIO_DIR, exist_ok=True)

def record_audio():
    print("Recording... Press 'q' to stop.")

    # List to store audio data
    audio_data = []

    # Callback function to continuously record audio
    def callback(indata, frames, time, status):
        if status:
            print(status)
        audio_data.append(indata.copy())

    # Start streaming audio input
    with sd.InputStream(samplerate=SAMPLE_RATE, channels=CHANNELS, callback=callback):
        while not keyboard.is_pressed("q"):
            pass

    print("\nRecording stopped. Saving audio file...")

    # Convert list to numpy array
    audio_array = np.concatenate(audio_data, axis=0)

    # Save as WAV file
    wav.write(AUDIO_FILE, SAMPLE_RATE, (audio_array * 32767).astype(np.int16))
    
    print(f"Audio saved as: {AUDIO_FILE}")

if __name__ == "__main__":
    record_audio()
