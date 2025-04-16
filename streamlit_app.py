import streamlit as st
import asyncio
from main import run_blog_pipeline
import tempfile
import os
import textstat

st.set_page_config(page_title="AI Blog Writer", layout="wide")

st.title("🧠 Autonomous AI Blog Writer")
st.markdown("Give it a topic, and it will research, write, optimize, and export a blog — all smartly and autonomously.")

if "blog_md" not in st.session_state:
    st.session_state.blog_md = None
if "metadata" not in st.session_state:
    st.session_state.metadata = None
# --- Input form ---
with st.form("blog_form"):
    topic = st.text_input("📌 Blog Topic", placeholder="e.g. How Python is used in AI")
    tone = st.selectbox("✍️ Tone", options=["educational", "creative", "technical", "formal","beginner-friendly"], index=0)
    submitted = st.form_submit_button("🚀 Generate Blog")




if submitted and topic:
    async def streamlit_runner():
        with st.spinner("Running blog pipeline..."):
            blog_md, metadata = await run_blog_pipeline(topic, tone, "blogs", return_data=True)
            st.session_state.blog_md = blog_md
            st.session_state.metadata = metadata
            st.success("✅ Blog generated successfully!")

    asyncio.run(streamlit_runner())

# --- Display Output if present ---
if st.session_state.blog_md and st.session_state.metadata:
    st.subheader("📄 Blog Content")
    st.markdown(st.session_state.blog_md, unsafe_allow_html=True)

    st.subheader("📦 Metadata")
    st.json(st.session_state.metadata)

    st.download_button("⬇️ Download Blog Markdown",
                       st.session_state.blog_md,
                       file_name="blog.md")

    st.download_button("⬇️ Download Metadata JSON",
                       str(st.session_state.metadata),
                       file_name="metadata.json")
    st.subheader("📊 Readability Score")
    plain_text = st.session_state.blog_md.replace("#", "").replace("*", "")
    ease_score = textstat.flesch_reading_ease(plain_text)
    grade_score = textstat.flesch_kincaid_grade(plain_text)

    st.markdown(f"""
    - **Flesch Reading Ease**: {ease_score:.2f}  
    - **Flesch-Kincaid Grade Level**: {grade_score:.2f}
    """)

   