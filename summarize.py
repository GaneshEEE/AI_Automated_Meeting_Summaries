import google.generativeai as genai

# Set up Gemini API key
genai.configure(api_key="AIzaSyACh0qNaMehr84I1hum2AcHi9Mf0VLapNQ")

# Load transcript
with open("transcription.txt", "r") as file:
    text = file.read()

# Use the latest Gemini model
model = genai.GenerativeModel("gemini-1.5-pro-latest")

# Generate summary
response = model.generate_content(f"Summarize this text in bullet points (Include as much detail as needed, but keep it short and precise):\n\n{text}")

# Save summary to a file
with open("summary.txt", "w") as file:
    file.write(response.text)

print("✅ Summary created! Check 'summary.txt'")
