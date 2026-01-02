import streamlit as st
from google import genai
import os

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="GameMaster AI 🎮",
    layout="wide"
)

# ---------------- API CLIENT ----------------
client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

MODEL_ID = "models/gemini-1.5-pro-latest"

# ---------------- HELPER ----------------
def generate(prompt):
    response = client.generate_content(
        model=MODEL_ID,
        contents=prompt
    )
    return response.text

# ---------------- UI ----------------
st.title("🎮 GameMaster AI – Ultimate Game Studio Agent")

tabs = st.tabs([
    "🧠 Game Concept",
    "🌍 Level Design",
    "🤖 NPC Behavior",
    "⚔️ Strategy",
    "📜 Story & Dialogue"
])

with tabs[0]:
    idea = st.text_area(
        "Describe your game idea",
        placeholder="A cyberpunk RPG set in Mumbai with AI gangs..."
    )
    if st.button("Generate Game Concept"):
        out = generate(
            f"Create a detailed game concept with genre, storyline, and core mechanics:\n{idea}"
        )
        st.markdown(out)

with tabs[1]:
    if st.button("Generate Level Design"):
        out = generate(
            "Design 3 game levels with environment, terrain, and challenges."
        )
        st.markdown(out)

with tabs[2]:
    if st.button("Generate NPC Behaviors"):
        out = generate(
            "Create intelligent NPC behavior rules for enemies, allies, and civilians."
        )
        st.markdown(out)

with tabs[3]:
    if st.button("Generate Game Strategy"):
        out = generate(
            "Suggest player engagement and balancing strategies for a modern game."
        )
        st.markdown(out)

with tabs[4]:
    if st.button("Generate Story & Dialogues"):
        out = generate(
            "Write interactive quests and branching dialogues for a game."
        )
        st.markdown(out)

