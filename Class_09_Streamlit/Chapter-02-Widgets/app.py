import streamlit as st

st.title("Kyma AI Student Registration Portal")

# Button
if st.button("Register for AI & RAG Development"):
    st.success(" Registration request submitted successfully!")

# Checkbox
join_internship = st.checkbox("Apply for Kyma AI Internship")

if join_internship:
    st.write(" You have selected the Internship Program.")

# Radio Button
learning_mode = st.radio(
    "Choose Your Learning Mode:",
    ["Online", "Offline", "Hybrid"]
)
st.write(f" Learning Mode: {learning_mode}")

# Select Box
course = st.selectbox(
    "Choose Your AI Course:",
    [
        "Python Programming",
        "Generative AI",
        "Machine Learning",
        "AI & RAG Development"
    ]
)
st.write(f" Selected Course: {course}")

# Slider
study_hours = st.slider(
    "Daily AI Practice Hours",
    1,
    10,
    2
)
st.write(f" Daily Study Hours: {study_hours} hour(s)")

# Number Input
projects = st.number_input(
    "How many AI projects have you completed?",
    min_value=0,
    max_value=50,
    step=1
)
st.write(f"Projects Completed: {projects}")

# Text Input
name = st.text_input("Enter Your Full Name")

if name:
    st.write(f"👋 Welcome, {name}! Let's begin your AI journey with Kyma AI.")

# Date Input
joining_date = st.date_input("Select Your Course Joining Date")

st.write(f"Joining Date: {joining_date}")