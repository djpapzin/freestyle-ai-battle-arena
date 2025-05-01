import streamlit as st
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))
# Fix imports for compatibility with different environments
from openai_utils import generate_rap
from elevenlabs_utils import text_to_speech_elevenlabs

def generate_beats_lyrics():
    st.title("🎶 Generate Lyrics")

    lyrics_input = st.text_area("Enter your Lyrics:")

    if st.button("Generate AI Rap with Voice"):
        with st.spinner("Generating AI rap..."):
            ai_lyrics = generate_rap(lyrics_input)
            try:
                audio_path = text_to_speech_elevenlabs(ai_lyrics)
                st.success("✅ AI rap generated successfully!")
                st.audio(audio_path, format="audio/mp3")
                with open(audio_path, "rb") as f:
                    st.download_button("Download AI Rap", f, file_name="ai_rap.mp3", mime="audio/mpeg")
            except Exception as e:
                st.error(f"Error generating audio: {e}")
            st.text_area("🎵 AI Generated Lyrics:", ai_lyrics, height=200)

if __name__ == "__main__":
    generate_beats_lyrics()
