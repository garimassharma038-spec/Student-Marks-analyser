import streamlit as st
import pandas as pd

# App Title
st.title("📊 Student Marks Analyzer with Visualization")

# Student Details
name = st.text_input("Enter Student Name")

# Marks Input
st.subheader("Enter Marks")
m1 = st.number_input("Subject 1 Marks", min_value=0, max_value=100, value=0)
m2 = st.number_input("Subject 2 Marks", min_value=0, max_value=100, value=0)
m3 = st.number_input("Subject 3 Marks", min_value=0, max_value=100, value=0)

# Calculate Results
if st.button("Calculate Result"):

    total = m1 + m2 + m3
    average = total / 3

    # Grade Calculation
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "Fail"

    # Display Results
    st.header("Result Summary")
    st.write("**Student Name:**", name)
    st.write("**Total Marks:**", total)
    st.write("**Average Marks:**", round(average, 2))
    st.write("**Grade:**", grade)

    # Create DataFrame
    df = pd.DataFrame({
        "Subjects": ["Subject 1", "Subject 2", "Subject 3"],
        "Marks": [m1, m2, m3]
    })

    # Visualizations
    st.subheader("📈 Marks Comparison")
    st.bar_chart(df.set_index("Subjects"))

    st.subheader("📉 Marks Trend")
    st.line_chart(df.set_index("Subjects"))

    # Table
    st.subheader("📋 Marks Table")
    st.dataframe(df, use_container_width=True) 
