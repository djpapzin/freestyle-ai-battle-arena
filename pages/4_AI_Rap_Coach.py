import streamlit as st
import os
import sys

# Add parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))

# Fix imports for compatibility with different environments
from openai_utils import coach_rap

def ai_rap_coach():
    st.title("🎤 AI Rap Coach")

    rap_text = st.text_area("Paste your Rap:")

    if st.button("Analyze Rap"):
        feedback = coach_rap(rap_text)
        st.markdown("## 📋 Feedback:")
        st.markdown(feedback)

if __name__ == "__main__":
    ai_rap_coach()
