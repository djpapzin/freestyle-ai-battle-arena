import requests

# Add your AssemblyAI API key here
ASSEMBLYAI_API_KEY = "YOUR_ASSEMBLYAI_API_KEY"

def speech_to_text_assemblyai(audio_file_path):
    headers = {
        "authorization": ASSEMBLYAI_API_KEY,
        "content-type": "application/json"
    }

    # Upload audio
    with open(audio_file_path, 'rb') as f:
        upload_response = requests.post(
            'https://api.assemblyai.com/v2/upload',
            headers={"authorization": ASSEMBLYAI_API_KEY},
            files={"file": f}
        )
    audio_url = upload_response.json()['upload_url']

    # Start transcription
    transcript_response = requests.post(
        "https://api.assemblyai.com/v2/transcript",
        json={"audio_url": audio_url},
        headers=headers
    )
    transcript_id = transcript_response.json()['id']

    # Poll for completion
    while True:
        polling_response = requests.get(
            f"https://api.assemblyai.com/v2/transcript/{transcript_id}",
            headers=headers
        )
        status = polling_response.json()['status']
        if status == 'completed':
            return polling_response.json()['text']
        elif status == 'error':
            raise Exception(f"Transcription failed: {polling_response.json()['error']}")
