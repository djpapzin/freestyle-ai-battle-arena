from openai import OpenAI
import os


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Load from environment variable


def generate_rap(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {
                "role": "system",
                "content": "You are a skilled battle rapper. Generate punchy, rhyming rap lyrics in a freestyle style."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content.strip()

def analyze_rap(rap_text):
    prompt = f"Analyze this rap for punchlines, flow, and rhyme: {rap_text}. Give a score out of 10 for each."

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "system", "content": "You are a rap critic who scores lyrics."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()

# ✅ NEW function for AI Rap Coach
def coach_rap(rap_text):
    prompt = f"""
You're an expert rap coach. Analyze the following rap and provide:

1. **Strong Points** 🔥  
2. **Weak Points** ❌  
3. **Suggestions for Improvement** 💡  
4. **Score out of 10** for:
   - Flow
   - Lyrics
   - Rhyme

Rap:
{rap_text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "system", "content": "You are a professional rap coach giving detailed feedback."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()
