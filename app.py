import streamlit as st

def home():
    st.set_page_config(page_title="Freestyle AI Battle Arena", layout="centered")

    # Top-right login/signup buttons
    col1, col2, col3 = st.columns([6, 1, 1])
    with col2:
        if st.button("Login"):
            st.info("🔐 Login functionality coming soon!")  # Placeholder
    with col3:
        if st.button("Sign Up"):
            st.info("📝 Sign-up functionality coming soon!")  # Placeholder

    # Custom freestyle-styled UI
    st.markdown(
        """
        <style>
        body {
            background-color: #0f0c29;
        }
        .main-container {
            background: linear-gradient(135deg, #0f0c29, #302b63, #ff0080);
            border-radius: 20px;
            padding: 60px 40px;
            color: white;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.4);
            text-align: center;
            animation: fadeIn 1.2s ease-in-out;
        }
        .title {
            font-size: 3.5em;
            font-weight: 900;
            letter-spacing: 2px;
            text-shadow: 2px 2px #000000;
            margin-bottom: 20px;
        }
        .description {
            font-size: 1.3em;
            color: #f1f1f1;
            margin-bottom: 30px;
            line-height: 1.6;
            font-style: italic;
        }
        .feature-highlight {
            font-size: 1.05em;
            color: #ffffff;
            background-color: rgba(0, 0, 0, 0.3);
            padding: 12px 25px;
            border-radius: 12px;
            display: inline-block;
            margin-top: 15px;
            box-shadow: 0 0 10px #ff0080;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        </style>

        <div class="main-container">
            <div class="title">🎤 Freestyle AI Battle Arena</div>
            <div class="description">
                Enter the world of AI-powered rap battles and creativity. Whether you're a rap enthusiast or a total beginner, our platform helps you freestyle, learn, and level up your bars.
            </div>
            <div class="feature-highlight">
                💥 Rap Coach &nbsp; • &nbsp; 🎶 AI Beats & Rhymes &nbsp; • &nbsp; 🥊 Battle Mode: AI or Player
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    home()
