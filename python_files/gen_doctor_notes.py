import openai
import os
from dotenv import load_dotenv


# Set your OpenAI API key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

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

# Function to format the text into structured doctor notes
def format_doctor_notes(transcribed_text):
    client = openai.OpenAI(api_key=OPENAI_API_KEY)  # Initialize the OpenAI client
    
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

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Could change to gpt-4 if needed
        messages=[{"role": "system", "content": "You are a medical assistant generating structured doctor notes."},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

def gen_notes(): 
    transcribed_text = read_transcription(TRANSCRIPTION_FILE)
    
    if transcribed_text:
        formatted_notes = format_doctor_notes(transcribed_text)
        
        # Save formatted notes to a file
        output_file = "results/doctor_notes.txt"
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(formatted_notes)
        
        print("Doctor notes successfully generated and saved to:", output_file)
    else:
        print("No transcription found. Please check the transcription file.")
# Main execution
if __name__ == "__main__":
    gen_notes()
