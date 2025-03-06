import openai
import os

# Set your OpenAI API key (Make sure to use environment variables or a config file in production)
OPENAI_API_KEY = "your-api-key-here"

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
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a medical assistant generating structured doctor notes."},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

# Main execution
if __name__ == "__main__":
    transcribed_text = read_transcription(TRANSCRIPTION_FILE)
    
    if transcribed_text:
        formatted_notes = format_doctor_notes(transcribed_text)
        
        # Save formatted notes to a file
        output_file = "transcribed_audio/doctor_notes.txt"
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(formatted_notes)
        
        print("Doctor notes successfully generated and saved to:", output_file)
    else:
        print("No transcription found. Please check the transcription file.")
