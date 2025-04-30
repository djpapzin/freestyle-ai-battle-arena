import streamlit as st
from utils.minimax_utils import (
    generate_rap_response,
    generate_rap_audio,
    get_generated_audio_url,
    download_audio,
)

st.set_page_config(page_title="🔥 Rap Battle Generator", layout="centered")

st.title("🎤 AI Rap Battle Generator")
st.markdown("Generate rap battle responses with AI and turn them into 🔊 music!")

# --- User Inputs ---
opponent_rap = st.text_area("Enter opponent's rap (any number of lines):", height=150)

num_lines = st.slider("How many lines should the AI generate?", min_value=2, max_value=16, value=6, step=2)

generate_button = st.button("Generate Rap 🔥")

if generate_button and opponent_rap.strip():
    with st.spinner("Generating rap lyrics..."):
        try:
            rap_response = generate_rap_response(opponent_rap, num_lines=num_lines)
            st.success("✅ Rap Generated!")
            st.text_area("AI's Rap Response:", rap_response, height=150)

            with st.spinner("Generating audio... 🎶"):
                generation_id, headers = generate_rap_audio(rap_response)
                audio_url = get_generated_audio_url(headers, generation_id)
                audio_file = download_audio(audio_url)

                st.success("🎵 Audio Ready!")

                with open(audio_file, "rb") as f:
                    st.audio(f.read(), format="audio/mp3")
                    st.download_button("Download MP3", f, file_name="rap_response.mp3")
        except Exception as e:
            st.error(f"Something went wrong: {str(e)}")
