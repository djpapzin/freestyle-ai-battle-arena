import os
import requests
import time
from openai import OpenAI

AIML_API_KEY = "REMOVED_AIML_KEY"
client = OpenAI(
    base_url="https://api.aimlapi.com/v1",
    api_key=AIML_API_KEY,
)

# ----------- RAP GENERATION -----------
def generate_rap_response(opponent_rap, num_lines=6, model="gpt-4o"):
    prompt = f"""
You are an aggressive, clever, and witty battle rapper. Respond to the opponent's rap creatively with punchlines and tight rhymes ({num_lines} lines).
Your style should feel natural and ready for a rap battle stage.

Opponent's Rap:
{opponent_rap}

Your Rap Response:
"""

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an elite battle rapper skilled in punchlines and rhythm."},
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content.strip()

# ----------- AUDIO GENERATION -----------
def generate_rap_audio(rap_response, reference_audio_url=None):
    url_generate = "https://api.aimlapi.com/v2/generate/audio"

    if reference_audio_url is None:
        reference_audio_url = "https://tand-dev.github.io/audio-hosting/spinning-head-271171.mp3"

    prompt = f"##{rap_response}##"

    payload = {
        "model": "minimax-music",
        "reference_audio_url": reference_audio_url,
        "prompt": prompt,
    }

    headers = {
        "Authorization": f"Bearer {AIML_API_KEY}",
        "Content-Type": "application/json",
    }

    post_response = requests.post(url_generate, json=payload, headers=headers)

    if post_response.status_code != 201:
        raise Exception(f"Error starting generation: {post_response.text}")

    generation_id = post_response.json().get('id')
    return generation_id, headers

def get_generated_audio_url(headers, generation_id):
    url_check = "https://api.aimlapi.com/v2/generate/audio"
    params = {"generation_id": generation_id}

    while True:
        get_response = requests.get(url_check, params=params, headers=headers)

        if get_response.status_code != 200:
            raise Exception(f"Error retrieving generation: {get_response.text}")

        music_info = get_response.json()
        status = music_info.get('status')

        if status == 'completed':
            audio_url = music_info.get('audio_file', {}).get('url')
            if not audio_url:
                raise Exception(f"No audio URL returned: {music_info}")
            return audio_url
        elif status == 'error':
            error_detail = music_info.get('error', {}).get('detail')
            error_message = error_detail[0].get('msg', 'Unknown error') if error_detail else 'Unknown error'
            raise Exception(f"Music generation failed: {error_message}")
        else:
            time.sleep(5)

def download_audio(audio_url, output_filename="final_rap_output.mp3"):
    audio_data = requests.get(audio_url)
    if audio_data.status_code != 200:
        raise Exception(f"Failed to download audio: {audio_data.status_code}")

    with open(output_filename, "wb") as f:
        f.write(audio_data.content)

    return output_filename
