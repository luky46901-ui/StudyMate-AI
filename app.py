
import streamlit as st
import random
import re

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📚",
    layout="centered"
)

st.title("📚 StudyMate AI")
st.subheader("Your Personal AI Study Companion")
st.write(
    "Turn your notes into simple explanations and practice quizzes."
)

st.divider()

st.header("1. 📖 Add Your Study Material")
material = st.text_area(
    "Paste your notes or textbook content here",
    height=220,
    placeholder="Paste your study notes here..."
)

st.divider()

st.header("2. 💡 Understand Your Notes")
question = st.text_input(
    "What would you like to understand?",
    placeholder="Example: Explain binary search trees"
)

if st.button("Explain My Question", use_container_width=True):
    if not material.strip():
        st.warning("Please paste your study material first.")
    elif not question.strip():
        st.warning("Please enter a question.")
    else:
        words = re.findall(r"\b[\w'-]+\b", material)
        sentences = re.split(r"(?<=[.!?])\s+", material.strip())
        terms = [
            word.lower() for word in
            re.findall(r"\b[a-zA-Z]{4,}\b", question)
            if word.lower() not in {
                "explain", "what", "with", "about",
                "simple", "words", "give", "example"
            }
        ]

        relevant = [
            sentence for sentence in sentences
            if any(term in sentence.lower() for term in terms)
        ]

        st.markdown("### Explanation")
        if relevant:
            st.write(
                "Here is the relevant information from your notes:"
            )
            for sentence in relevant[:5]:
                st.write("- " + sentence.strip())
        else:
            st.info(
                "I couldn't find a direct match in your notes. "
                "Try using the main topic's exact words."
            )

        st.caption(
            "This free prototype extracts relevant sentences; "
            "it does not yet use a generative AI model."
        )

st.divider()

st.header("3. 📝 Practice Quiz")
quiz_topic = st.text_input(
    "Enter a topic for your quiz",
    placeholder="Example: Binary Search Trees"
)

if st.button("Create Practice Quiz", use_container_width=True):
    if not material.strip():
        st.warning("Please add study material first.")
    elif not quiz_topic.strip():
        st.warning("Please enter a quiz topic.")
    else:
        sentences = [
            s.strip() for s in
            re.split(r"(?<=[.!?])\s+", material.strip())
            if len(s.strip().split()) >= 5
        ]

        if len(sentences) < 2:
            st.warning(
                "Please paste at least two complete sentences "
                "so a practice quiz can be created."
            )
        else:
            random.seed(42)
            selected = sentences[:5]
            st.session_state.quiz = selected
            st.session_state.quiz_topic = quiz_topic
            st.session_state.quiz_answers = {}

if "quiz" in st.session_state:
    st.markdown(f"### Quiz: {st.session_state.quiz_topic}")
    st.write(
        "Choose the sentence that best matches each question."
    )

    for i, answer in enumerate(st.session_state.quiz):
        options = [answer]
        for other in st.session_state.quiz:
            if other != answer:
                options.append(other)
            if len(options) == min(4, len(st.session_state.quiz)):
                break

        options = list(dict.fromkeys(options))
        st.session_state.quiz_answers[i] = st.radio(
            f"Question {i + 1}: Which statement appeared in your notes?",
            options,
            key=f"quiz_{i}"
        )

    if st.button("Check My Answers", use_container_width=True):
        score = 0
        for i, correct in enumerate(st.session_state.quiz):
            if st.session_state.quiz_answers.get(i) == correct:
                score += 1

        st.success(
            f"Your score: {score}/{len(st.session_state.quiz)}"
        )
        st.write("Review the correct statements:")
        for i, correct in enumerate(st.session_state.quiz):
            st.write(f"{i + 1}. {correct}")

st.divider()
st.caption("StudyMate AI | Multimodal AI Hackathon 2026")
