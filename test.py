import subprocess

audio_file = "audio_files/recorded_audio.wav"  # Use the correct path to your audio file
ffmpeg_path = r"C:\ffmpeg\ffmpeg-7.1-essentials_build\ffmpeg-7.1-essentials_build\bin\ffmpeg.exe"  # Adjust this path to where FFmpeg is located
output_file = "audio_files/recorded_audio.mp3"  # Specify an output file (you can choose any format)

# Run a simple FFmpeg command to test the integration
subprocess.run([ffmpeg_path, "-i", audio_file, output_file])  # Use ffmpeg_path instead of just "ffmpeg"
