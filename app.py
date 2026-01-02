import streamlit as st
from google import genai
import os
import json
import requests

# ------------------- CONFIG -------------------
st.set_page_config(
    page_title="GameMaster AI",
    page_icon="🎮",
    layout="wide"
)

# ------------------- GEMINI CLIENT -------------------
from google import genai
import os

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def generate(prompt):
    response = client.models.generate_content(
        model="gemini-1.5-pro-latest",
        contents=prompt
    )
    return response.text


# ------------------- LOTTIE LOADER -------------------
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ------------------- UI -------------------
st.markdown("""
<style>
.big-title { font-size:40px; font-weight:800; }
.card { background:#111; padding:20px; border-radius:15px; margin-bottom:15px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">🎮 GameMaster AI</div>', unsafe_allow_html=True)
st.caption("Your AI-powered Game Design & Strategy Partner")

# ------------------- ANIMATION -------------------
lottie_game = load_lottie("https://assets10.lottiefiles.com/packages/lf20_qp1q7mct.json")

col1, col2 = st.columns([1,2])

with col1:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/4712/4712109.png",
        width=220,
        caption="GameMaster Avatar"
    )

with col2:
    if lottie_game:
        from streamlit_lottie import st_lottie
        st_lottie(lottie_game, height=260)

# ------------------- FEATURES -------------------
feature = st.selectbox(
    "Select GameMaster Skill",
    [
        "🎮 Game Concept Generator",
        "🗺 Level & Environment Designer",
        "🤖 NPC Behavior Designer",
        "📊 Game Strategy Assistant",
        "💬 Dialogue & Story Scripting"
    ]
)

idea = st.text_area(
    "Describe your game idea / requirement",
    height=120,
    placeholder="Example: Open-world RPG with mythological elements..."
)

# ------------------- PROMPT ENGINE -------------------
def build_prompt(feature, idea):
    return f"""
You are GameMaster AI, a professional game development assistant.

Feature: {feature}

User Input:
{idea}

Generate structured, creative, and practical output.
Use bullet points, sections, and clear explanations.
"""

# ------------------- RUN -------------------
if st.button("🚀 Generate", use_container_width=True):
    if not idea.strip():
        st.warning("Please enter an idea")
    else:
        with st.spinner("GameMaster AI is thinking..."):
            output = generate(build_prompt(feature, idea))

        st.markdown("### 🧠 AI Output")
        st.markdown(f"<div class='card'>{output}</div>", unsafe_allow_html=True)

        # ------------------- DOWNLOAD -------------------
        st.download_button(
            label="📥 Download Result",
            data=output,
            file_name="gamemaster_ai_output.txt",
            mime="text/plain"
        )
