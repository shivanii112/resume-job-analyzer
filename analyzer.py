"""
analyzer.py
-----------
Resume ↔ Job Match Analyzer using Gemini with PDF support (google.genai).

Design:
- Native PDF input (no text extraction)
- Raw text output
- No JSON
- No system_instruction
"""

from typing import Optional
from pathlib import Path

from google.genai.types import Part
from config import get_gemini_model
from prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE

MODEL_NAME = "gemini-flash-lite-latest"


def load_pdf_as_part(pdf_path: str) -> Part:
    """
    Load a PDF file and convert it into a Gemini Part (google.genai compatible).
    """
    pdf_bytes = Path(pdf_path).read_bytes()

    return Part(
        inline_data={
            "mime_type": "application/pdf",
            "data": pdf_bytes
        }
    )


def analyze_resume_job_match_pdf(
    resume_pdf_path: str,
    job_pdf_path: str
) -> Optional[str]:
    """
    Analyze resume PDF against job description PDF using Gemini.

    Returns:
        Raw Gemini response text
    """

    try:
        client = get_gemini_model()

        resume_part = load_pdf_as_part(resume_pdf_path)
        job_part = load_pdf_as_part(job_pdf_path)

        prompt = (
            SYSTEM_PROMPT.strip()
            + "\n\n"
            + USER_PROMPT_TEMPLATE.replace(
                "{resume_text}", "Refer to the attached RESUME PDF."
            ).replace(
                "{job_text}", "Refer to the attached JOB DESCRIPTION PDF."
            )
        )

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=[
                prompt,
                resume_part,
                job_part
            ]
        )

        return response.text

    except Exception as e:
        return f"❌ Gemini call failed: {str(e)}"
