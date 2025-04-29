
import requests

# ⚠️ Use your real API key here (not recommended for production)
ELEVEN_LABS_API_KEY = "REMOVED_ELEVEN_LABS_KEY"
VOICE_ID = "bP8FJDHmWVEgXJDitdQd"

def text_to_speech_elevenlabs(text, filename="ai_rap.mp3"):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"

    headers = {
        "Accept": "audio/mpeg",
        "xi-api-key": ELEVEN_LABS_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.4,
            "similarity_boost": 0.7
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        return filename
    else:
        raise Exception(f"Failed to generate voice: {response.text}")
