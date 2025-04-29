# === FILE: Home.py ===
import streamlit as st


def main():
    st.set_page_config(page_title="Freestyle AI Battle Arena", layout="wide")
    st.markdown("<h1 style='text-align: center;'>🎤 Freestyle AI Battle Arena</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Battle an AI rapper, generate beats & lyrics, or get coached!</p>", unsafe_allow_html=True)

    # Left Menu
    with st.sidebar:
        st.header("Navigation")
        st.page_link("Home.py", label="🏠 Home", icon="🏠")
        st.page_link("pages/1_Freestyle_Battle.py", label="🤼‍♂️ Freestyle Battle")
        st.page_link("pages/2_Generate_Beats_Lyrics.py", label="🎶 Generate Beats + Lyrics")
        st.page_link("pages/3_AI_Rap_Coach.py", label="🎤 AI Rap Coach")

if __name__ == "__main__":
    main()