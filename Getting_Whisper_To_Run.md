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

Continue back to ReadMe.md steps, whisper will be installed with the requirements