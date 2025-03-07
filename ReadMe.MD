How to Setup
-------------------------------------------------------------------------------------------
1. Install Open AI's Whisper Model

    Getting the Whisper AI model to run locally on a Windows computer takes some setup steps:
    youtube tutorial: https://www.youtube.com/watch?v=ABFqbY_rmEk

    1. I used python version 3.10. It can be installed here: https://www.python.org/downloads/release/python-3100/

    2. Install pytorch: https://pytorch.org/get-started/locally/
    Choose cuda option if you have an nvidia gpu (You m ay also need nvidia drivers and cuda installed for this to work)
otherwise choose CPU option for Compute Platform (I use the cuda version which utlizes my gpu when running pytorch)


    2. Install Windows package manager: Follow this link: https://chocolatey.org/install#individual
    or
    Open powershell as administrator and run this: Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

3. Install ffmpeg:
In powershell run: choco install ffmpeg
-------------------------------------------------------------------------------------------
2. Setting up Virtual Environment
    Create Virtual Environment:
    python -m venv venv

    Activate Virtual Environment:
    Mac/Linux:
    source venv/bin/activate
    Windows:
    Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
    venv\Scripts\Activate.ps1

    Install Requirements:
    pip install -r requirements.txt
-------------------------------------------------------------------------------------------
3. Running the Application
    There are 4 files
    record_audio.py → Records patient conversation and stores .mp4 in /audio_files
    audio_to_text.py → Transcribes audio and stores .txt in /transcribed_audio
    gen_doctor_notes.py → Formats transcription into doctor notes and stores the notes in results
    main.py → this is where all 3 files are connected to make a complete application

    To run: python python_files/main.py

    you can also run each file induviually for testing

    Special Note:
    API key for open ai is stored in a .env that I have stored locally. I do not want to push this key to a public github so you can create a .env file yourself and either generate your own API key or ask me for mine and I can send it.