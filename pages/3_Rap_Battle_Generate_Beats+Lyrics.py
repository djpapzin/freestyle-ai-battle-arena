import streamlit as st
from utils.minimax_utils import (
    generate_rap_response,
    generate_rap_audio,
    get_generated_audio_url,
    download_audio,
)

st.set_page_config(page_title="🎤 AI Rap Generator", layout="centered")

st.title("🎶 AI Rap Battle Generator")

# --- Input Fields ---
opponent_rap = st.text_area("Enter opponent's rap (any lines):", height=150)

num_lines = st.slider("How many lines should the AI generate?", 2, 16, value=6, step=2)

voice_style = st.selectbox("Choose voice style for AI:", ["Aggressive", "Calm", "Robotic", "Playful", "Sarcastic"])

music_style = st.selectbox("Choose background music style:", ["Hip-hop", "Trap", "Lo-fi", "Boom Bap"])

generate_button = st.button("🔥 Generate My Rap")

if generate_button and opponent_rap.strip():
    with st.spinner("Writing rap lyrics... ✍️"):
        try:
            rap_response = generate_rap_response(opponent_rap, num_lines=num_lines, voice_style=voice_style)
            st.success("✅ Rap generated!")
            st.text_area("AI's Rap Response:", rap_response, height=150)

            with st.spinner("Creating audio... 🎵"):
                generation_id, headers = generate_rap_audio(rap_response, music_style)
                audio_url = get_generated_audio_url(headers, generation_id)
                audio_file = download_audio(audio_url)

                st.success("🎧 Audio ready!")

                with open(audio_file, "rb") as f:
                    st.audio(f.read(), format="audio/mp3")
                    st.download_button("Download MP3", f, file_name="rap_response.mp3")
        except Exception as e:
            st.error(f"Error: {str(e)}")
