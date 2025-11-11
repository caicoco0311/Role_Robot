import streamlit as st
from openai import OpenAI

# -----------------------
# Page Configuration
# -----------------------
st.set_page_config(page_title="Ask Me Anything", layout="wide")

# Custom CSS for background color
st.markdown(
    """
    <style>
        body {
            background-color: #E6F2FF; /* 淡蓝色背景 */
        }
        .stApp {
            background-color: #E6F2FF;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------
# Title Section
# -----------------------
st.title("🤖 Role_Based Robot")
st.write("💭 Choose the aspect you are interested in")

# -----------------------
# Sidebar: API Key + Role Selection
# -----------------------
st.sidebar.header("🔑 API & Role Settings")

# API key input
api_key = st.sidebar.text_input(
    "Enter your OpenAI API Key:",
    type="password",
    placeholder="sk-xxxxxxxxxxxxxxxx",
)

# Role selection
roles = {
    "🧠 Philosopher": 
    "You are a philosopher. You respond with depth, questioning assumptions, and exploring meaning. Every answer should provoke reflection — you seek truth, not certainty.",

    "🪞 Psychologist": 
    "You are a psychologist. You interpret human behavior, emotion, and cognition with empathy and logic. Always connect ideas to motivation, perception, and memory.",

    "🚀 Sci-Fi Writer": 
    "You are a science fiction writer. Imagine alternate worlds, near futures, and human-machine relationships. Answer with creative world-building and speculative tone.",

    "🎭 Poet": 
    "You are a poet. Express everything in rhythm, metaphor, and emotion. Your words should feel like music — vivid, lyrical, and full of imagery.",

    "📸 Photographer": 
    "You are a photographer. Describe scenes through composition, light, and texture. Every idea should feel like a frame of a film — visual, atmospheric, and cinematic.",

    "🏛️ Architect": 
    "You are an architect. You think in structure, balance, and proportion. Relate ideas to space, rhythm, material, and human experience within design."
}

role_name = st.sidebar.selectbox("Choose a role:", list(roles.keys()))
role_description = roles[role_name]
st.sidebar.info(role_description)

# -----------------------
# User Input Area
# -----------------------
user_input = st.text_area(
    "💬 Enter your question or idea:",
    height=100,
    placeholder="e.g., How can I express sadness in movement?"
)

# -----------------------
# Generate Response
# -----------------------
if st.button("Generate Response"):
    if not api_key:
        st.warning("⚠️ Please enter your OpenAI API key in the sidebar.")
    elif not user_input:
        st.warning("Please enter a question first!")
    else:
        try:
            client = OpenAI(api_key=api_key)
            with st.spinner("AI is thinking..."):
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": role_description},
                        {"role": "user", "content": user_input}
                    ]
                )
                answer = response.choices[0].message.content
                st.success(f"🎬 {role_name} says:")
                st.write(answer)
        except Exception as e:
            st.error(f"Error: {e}")

# -----------------------
# Footer
# -----------------------
st.markdown("---")
st.caption("© caimingjun")
