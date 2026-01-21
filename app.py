
import tempfile
import streamlit as st

from analyzer import analyze_resume_job_match_pdf

st.set_page_config(
    page_title="Resume ↔ Job Match Analyzer",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Resume ↔ Job Match Analyzer")
st.subheader("Analyze your resume against a job description using Gemini AI")
st.markdown(
    """
Upload **PDF versions** of:
- Your **Resume**
- The **Job Description**

Gemini will analyze both and give you a detailed assessment.
"""
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader(
        "📄 Upload Resume (PDF)",
        type=["pdf"]
    )

with col2:
    job_file = st.file_uploader(
        "📄 Upload Job Description (PDF)",
        type=["pdf"]
    )

st.divider()

analyze_clicked = st.button("🔍 Analyze Match", type="primary")

if analyze_clicked:
    if not resume_file or not job_file:
        st.error("❌ Please upload both Resume and Job Description PDFs.")
    else:
        with st.spinner("Analyzing with Gemini..."):
            # Save uploaded files to temp paths
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as resume_tmp:
                resume_tmp.write(resume_file.read())
                resume_path = resume_tmp.name

            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as job_tmp:
                job_tmp.write(job_file.read())
                job_path = job_tmp.name

            result = analyze_resume_job_match_pdf(
                resume_pdf_path=resume_path,
                job_pdf_path=job_path
            )

        st.divider()

        st.subheader("📊 Analysis Result")

        if result.startswith("❌"):
            st.error(result)
        else:
            st.success("Analysis completed successfully!")
            st.markdown(result)

st.divider()

