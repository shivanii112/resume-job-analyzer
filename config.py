"""
config.py
---------
Centralized configuration for Gemini API access
(using the NEW google.genai SDK).
"""

import os
from dotenv import load_dotenv
from google import genai


def get_gemini_model():
    """
    Loads Gemini API key from environment variables and
    returns a configured Gemini client.

    Returns:
        genai.Client: Gemini client instance

    Raises:
        RuntimeError: If GEMINI_API_KEY is missing
    """

    # Load environment variables from .env
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "❌ GEMINI_API_KEY not found.\n"
            "➡️ Create a .env file and add:\n"
            "GEMINI_API_KEY=your_api_key_here"
        )

    # Initialize Gemini client (NEW SDK)
    client = genai.Client(api_key=api_key)

    return client
