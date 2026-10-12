
import streamlit as st

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📚",
    layout="centered"
)

st.title("📚 StudyMate AI")
st.subheader("Your Personal AI Study Companion")

st.write(
    "Learn from your study materials, understand difficult topics, "
    "and test your knowledge with practice questions."
)

st.divider()

st.header("📖 1. Add Your Study Material")

material = st.text_area(
    "Paste your notes or textbook content here:",
    height=200,
    placeholder="Paste your study material..."
)

st.header("❓ 2. Ask a Question")

question = st.text_input(
    "What would you like to understand?",
    placeholder="Ask a question about your notes..."
)

if st.button("Explain My Question", use_container_width=True):
    if not material.strip():
        st.warning("Please paste your study material first.")
    elif not question.strip():
        st.warning("Please enter a question.")
    else:
        st.info("Study material received!")
        st.write("**Your question:**", question)
        st.write("**Relevant study material:**")
        st.write(material)
        st.caption(
            "This prototype collects your question and notes. "
            "AI-generated answers will be added in the next development step."
        )

st.divider()

st.header("📝 3. Practice Quiz")

topic = st.text_input(
    "Enter a topic for your quiz:",
    placeholder="Example: Python loops"
)

if st.button("Create Practice Quiz", use_container_width=True):
    if topic.strip():
        st.write(f"Your practice quiz topic: **{topic}**")
        st.info(
            "Quiz generation will be connected in the next development step."
        )
    else:
        st.warning("Please enter a topic.")

st.divider()
st.caption("StudyMate AI | Built for the Multimodal AI Hackathon 2026")
