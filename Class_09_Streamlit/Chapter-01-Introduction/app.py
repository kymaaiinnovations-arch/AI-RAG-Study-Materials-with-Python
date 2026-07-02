import streamlit as st

st.title("Welcome to Kyma AI Innovations")

st.subheader("AI & RAG Development Course")

st.text("Welcome to your first interactive Streamlit application.")

st.write("Choose your preferred AI learning path.")

course = st.selectbox(
    "Select your AI Course:",
    [
        "Python Programming",
        "Generative AI",
        "Machine Learning",
        "AI & RAG Development"
    ]
)

st.write(f"You selected **{course}**. Great choice! Let's start your AI journey.")

st.success("Welcome to the Kyma AI Learning Platform!")
