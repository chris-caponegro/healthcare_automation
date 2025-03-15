import time
from record_audio import record_audio
from audio_to_text import transcribe_audio
from gen_doctor_notes_local_LLM import gen_notes

def main():
    print("Starting patient note recording process...\n")

    # Step 1: Record audio
    record_audio() # comment this out to avoid re recording
    time.sleep(2)  # Ensure file writes are complete

    # Step 2: Transcribe the recorded audio
    transcribe_audio()
    time.sleep(2)  # Allow processing time

    # Step 3: Generate formatted doctor notes
    gen_notes()

    print("Process completed successfully! Check the output files.\n")

if __name__ == "__main__":
    main()
