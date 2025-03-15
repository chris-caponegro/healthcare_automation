import ollama
import os

# Path to the transcribed text file
TRANSCRIPTION_FILE = "transcribed_audio/transcription.txt"

# Function to read the transcribed text
def read_transcription(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().strip()
    except FileNotFoundError:
        print("Error: Transcription file not found.")
        return None

# Function to format the text into structured doctor notes using Ollama
def format_doctor_notes(transcribed_text):
    prompt = f"""
    The following is a raw transcription of a conversation between a nurse and a patient. Convert it into structured doctor notes, summarizing key symptoms, patient history, and relevant medical details.

    --- Transcribed Conversation ---
    {transcribed_text}

    --- Expected Output ---
    Provide a well-structured summary suitable for a doctor's notes, including:
    - Patient's Chief Complaint
    - History of Present Illness (HPI)
    - Relevant Medical History
    - Current Symptoms
    - Any Prescribed Medications or Advice
    """

    response = ollama.chat(
        model="llama3.2:1b",  
        messages=[
            {"role": "system", "content": "You are a medical assistant generating structured doctor notes."},
            {"role": "user", "content": prompt}
        ]
    )

    return response['message']['content']

# Function to generate and save doctor notes
def gen_notes(): 
    transcribed_text = read_transcription(TRANSCRIPTION_FILE)
    
    if transcribed_text:
        formatted_notes = format_doctor_notes(transcribed_text)
        
        # Save formatted notes to a file
        output_file = "results/doctor_notes.txt"
        os.makedirs(os.path.dirname(output_file), exist_ok=True)  # Ensure directory exists
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(formatted_notes)
        
        print("Doctor notes successfully generated with llama3 and saved to:", output_file)
    else:
        print("No transcription found. Please check the transcription file.")
        
# Main execution
if __name__ == "__main__":
    gen_notes()
