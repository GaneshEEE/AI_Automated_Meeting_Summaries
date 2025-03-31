from faster_whisper import WhisperModel

# Force model to run on CPU (use "int8" for lower memory usage)
model = WhisperModel("small", device="cpu", compute_type="int8")

# Transcribe audio
segments, _ = model.transcribe("meeting_audio.mp3")

# Save full transcription to a text file
with open("transcription.txt", "w") as file:
    for segment in segments:
        file.write(segment.text + " ")

print("✅ Transcription completed! Check 'transcription.txt'")
