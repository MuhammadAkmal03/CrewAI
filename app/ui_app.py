import streamlit as st
from app.main_pipeline import generate_blog

st.title("🎬 YouTube → 📝 Blog Generator (CrewAI + Groq)")

topic = st.text_input("Enter topic to analyze YouTube videos:")

if st.button("Generate Blog"):
    with st.spinner("Analyzing YouTube videos + Writing blog..."):
        output = generate_blog(topic)

    st.success("Done!")
    st.markdown("## ✨ Final Blog")
    st.markdown(output)
