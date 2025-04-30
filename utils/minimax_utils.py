import os
import requests
import time
from openai import OpenAI

AIML_API_KEY = "REMOVED_AIML_KEY"
client = OpenAI(
    base_url="https://api.aimlapi.com/v1",
    api_key=AIML_API_KEY,
)

REFERENCE_AUDIO_MAP = {
    "Hip-hop": "https://tand-dev.github.io/audio-hosting/spinning-head-271171.mp3",
    "Trap": "https://tand-dev.github.io/audio-hosting/trap-beat.mp3",
    "Lo-fi": "https://tand-dev.github.io/audio-hosting/lofi-beat.mp3",
    "Boom Bap": "https://tand-dev.github.io/audio-hosting/boom-bap.mp3",
}

# --- RAP GENERATION ---
def generate_rap_response(opponent_rap, num_lines=6, voice_style="aggressive", model="gpt-4o"):
    prompt = f"""
You are a {voice_style.lower()} battle rapper. Respond creatively to the opponent's rap with tight rhymes and punchlines ({num_lines} lines).
Use the tone/style: {voice_style}.

Opponent's Rap:
{opponent_rap}

Your Rap Response:
"""

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": f"You are a {voice_style.lower()} battle rapper."},
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content.strip()

# --- AUDIO GENERATION ---
def generate_rap_audio(rap_response, music_style="Hip-hop"):
    url_generate = "https://api.aimlapi.com/v2/generate/audio"
    reference_audio_url = REFERENCE_AUDIO_MAP.get(music_style, REFERENCE_AUDIO_MAP["Hip-hop"])
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
