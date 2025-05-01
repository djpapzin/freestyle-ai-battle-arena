import streamlit as st
import sys
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))

# Fix imports for compatibility with different environments
from openai_utils import generate_rap
from openai_utils import analyze_rap

# Scoring Logic (You can move this to scoring_utils.py if you prefer)
def score_rap(rap_text):
    # Dummy logic: in a real scenario, this could be replaced by AI-based scoring
    import random
    return {
        "punchline": random.randint(1, 10),
        "flow": random.randint(1, 10),
        "rhyme": random.randint(1, 10)
    }

def calculate_total(score_dict):
    return sum(score_dict.values())

def declare_winner(score1, score2):
    total1 = sum(score1)
    total2 = sum(score2)
    if total1 > total2:
        return "🏆 Player 1 Wins!"
    elif total2 > total1:
        return "🏆 Player 2 Wins!" if len(score2) > 0 else "🏆 AI Wins!"
    else:
        return "🤝 It's a Tie!"

def freestyle_battle():
    st.set_page_config(page_title="Freestyle Battle", page_icon="🎤", layout="wide")
    st.title("🤼‍♂️ Freestyle Battle Arena")
    mode = st.radio("Choose Mode:", ["Player vs Player", "Player vs AI"])

    if "round" not in st.session_state:
        st.session_state.round = 1
        st.session_state.p1_scores = []
        st.session_state.p2_scores = []

    if mode == "Player vs Player":
        st.header(f"Round {st.session_state.round}/3")
        player1 = st.text_area("🎤 Player 1 Rap:")
        player2 = st.text_area("🎤 Player 2 Rap:")

        if st.button("Submit Round"):
            if player1 and player2:
                score1 = score_rap(player1)
                score2 = score_rap(player2)
                st.session_state.p1_scores.append(calculate_total(score1))
                st.session_state.p2_scores.append(calculate_total(score2))

                st.subheader("🔢 Scores This Round")
                col1, col2 = st.columns(2)
                with col1:
                    st.write("Player 1 Score", score1)
                with col2:
                    st.write("Player 2 Score", score2)

                st.session_state.round += 1

            if st.session_state.round > 3:
                winner = declare_winner(st.session_state.p1_scores, st.session_state.p2_scores)
                st.success(winner)
                st.session_state.round = 1
                st.session_state.p1_scores.clear()
                st.session_state.p2_scores.clear()

    elif mode == "Player vs AI":
        st.header(f"Round {st.session_state.round}/3")
        user_rap = st.text_area("🎤 Your Rap:")

        if st.button("Submit Round vs AI"):
            if user_rap:
                ai_rap = generate_rap(user_rap)
                score_user = score_rap(user_rap)
                score_ai = score_rap(ai_rap)
                st.session_state.p1_scores.append(calculate_total(score_user))
                st.session_state.p2_scores.append(calculate_total(score_ai))

                st.subheader("🤖 AI's Rap")
                st.success(ai_rap)

                st.subheader("🔢 Scores This Round")
                col1, col2 = st.columns(2)
                with col1:
                    st.write("Your Score", score_user)
                with col2:
                    st.write("AI Score", score_ai)

                st.session_state.round += 1

            if st.session_state.round > 3:
                winner = declare_winner(st.session_state.p1_scores, st.session_state.p2_scores)
                st.success(winner)
                st.session_state.round = 1
                st.session_state.p1_scores.clear()
                st.session_state.p2_scores.clear()

if __name__ == "__main__":
    freestyle_battle()
