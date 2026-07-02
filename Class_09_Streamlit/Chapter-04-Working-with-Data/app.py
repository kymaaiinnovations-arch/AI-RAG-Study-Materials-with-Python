import streamlit as st
import pandas as pd

# ==========================
# Chapter 4 - Working with Data
# Kyma AI Innovations
# ==========================

st.title("Kyma AI Student Dashboard")

st.write("Upload the student data CSV file to explore the dashboard.")

# Upload CSV
file = st.file_uploader(
    "Upload Student Data (CSV)",
    type=["csv"]
)

if file is not None:

    # Read CSV
    df = pd.read_csv(file)

    # Preview
    st.subheader("Student Data Preview")
    st.dataframe(df)

    # Statistics
    st.subheader("Dataset Summary")
    st.write(df.describe())

    # Filter by City
    st.subheader("Filter Students by City")

    cities = df["City"].unique()

    selected_city = st.selectbox(
        "Select City",
        cities
    )

    filtered_data = df[df["City"] == selected_city]

    st.dataframe(filtered_data)

    st.success(f"Showing students from {selected_city}")