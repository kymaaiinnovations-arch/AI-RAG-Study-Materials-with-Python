import streamlit as st

# ==========================
# Chapter 3 - Layouts
# Kyma AI Innovations
# ==========================

st.title(" Kyma AI Course Poll")

col1, col2 = st.columns(2)

with col1:
    st.header(" Generative AI")

    st.image(
        "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600",
        width=250
    )

    vote1 = st.button("Vote for Generative AI")

with col2:
    st.header("AI & RAG Development")

    st.image(
        "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=600",
        width=250
    )

    vote2 = st.button("Vote for AI & RAG")

if vote1:
    st.success("Thanks for voting for Generative AI!")

elif vote2:
    st.success("Thanks for voting for AI & RAG Development!")

# ==========================
# Sidebar
# ==========================

st.sidebar.title("Kyma AI Student Portal")

name = st.sidebar.text_input("Enter Your Name")

course = st.sidebar.selectbox(
    "Choose Your Course",
    [
        "Python Programming",
        "Generative AI",
        "Machine Learning",
        "AI & RAG Development"
    ]
)

if name:
    st.write(f" Welcome **{name}**!")

st.write(f" Selected Course: **{course}**")

# ==========================
# Expander
# ==========================

with st.expander(" How Kyma AI Learning Works"):
    st.write("""
1. Register for the AI Course.

2. Attend Live Interactive Classes.

3. Complete Weekly Assignments.

4. Build Real-World AI Projects.

5. Upload Your Projects to GitHub.

6. Earn Your Internship Certificate.
""")

# ==========================
# Markdown
# ==========================

st.markdown("---")

st.markdown(" Welcome to Kyma AI Innovations")

st.markdown("> **Learn AI. Build Projects. Shape Your Future.**")