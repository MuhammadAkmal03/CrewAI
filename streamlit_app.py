import streamlit as st
import time
import os
from datetime import datetime
from app.main_pipeline import run_pipeline
from app.config.llm_config import groq_llm

st.set_page_config(page_title="YouTube → Blog Generator", layout="wide")

# Big Title

st.markdown("<h1 style='font-size: 42px;'>📹 YouTube → 📝 Blog Generator</h1>", unsafe_allow_html=True)
st.write("Convert YouTube videos into high-quality blogs using AI.")

# Sidebar settings

model_choice = st.sidebar.selectbox(
    "Model",
    ["groq/llama-3.3-70b-versatile", "groq/llama-3.1-8b-instant"]
)

temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.3)

blog_length = st.sidebar.radio("Blog Length", ["Short", "Medium", "Long"])

include_faq = st.sidebar.checkbox("Include FAQ section")

groq_llm.model = model_choice
groq_llm.temperature = temperature

# MAIN INPUT

youtube_url = st.text_input("Enter YouTube Video URL")

# LOG AREA 

log_box = st.expander("Logs", expanded=False)
if "log_text" not in st.session_state:
    st.session_state.log_text = ""

def log(message):
    st.session_state.log_text += message + "\n"
    log_box.text_area("Execution Log", st.session_state.log_text, height=250)

# Generate Button

if st.button("Generate Blog"):

    if not youtube_url.strip():
        st.error("Please enter a valid YouTube URL.")
        st.stop()

    try:
        log("Starting pipeline...")
        with st.spinner("Extracting transcript..."):
            time.sleep(0.8)
            log("Transcript extracted.")

        with st.spinner("Summarizing content..."):
            time.sleep(0.8)
            log("Summary generated.")

        with st.spinner("Writing blog..."):
            blog_content = run_pipeline(youtube_url)
            log("Blog writing complete.")

        st.success("Blog generated successfully!")
        st.subheader("Blog Output")
        st.markdown(blog_content)

        os.makedirs("outputs", exist_ok=True)
        file_path = f"outputs/blog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(blog_content)

        st.download_button(
            "Download Blog",
            data=blog_content,
            file_name="blog.md",
            mime="text/markdown"
        )

    except Exception as e:
        st.error(f"Error: {str(e)}")
        log(f"Error: {str(e)}")
