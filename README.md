# 🎯 Resume ↔ Job Match Analyzer (PDF-Based)

A Streamlit web application that analyzes a **resume PDF** against a **job description PDF** using **Google Gemini AI** and provides a detailed, human-readable assessment.

This project leverages **Gemini’s native PDF understanding** (no OCR or text extraction libraries) and returns **raw analysis text** for maximum stability and reliability.

---

## 🚀 Key Features

- 📄 Upload **Resume PDF**
- 📄 Upload **Job Description PDF**
- 🤖 Analyze using **Google Gemini (free tier)**
- 🧠 Native PDF understanding (no parsing hacks)
- 📝 Raw, natural-language analysis output
- 🌐 Simple and clean **Streamlit UI**
- ⚡ Fast and reliable (no JSON parsing failures)

---

## 🛠️ Tech Stack

- **Python** 3.9+
- **Streamlit** – Web UI
- **Google Gemini API** (AI Studio, API-key based)
- **google-genai SDK**
- **dotenv** – Environment variable management

---

## 📂 Project Structure

resume-job-analyzer/
├── app.py # Streamlit UI
├── analyzer.py # Gemini PDF analysis logic
├── prompts.py # Prompt templates
├── config.py # Gemini client setup
├── sample_resume.pdf # Sample resume (PDF)
├── sample_job.pdf # Sample job description (PDF)
├── requirements.txt # Dependencies
├── .env.example # Environment variable template
├── .gitignore # Git ignore rules
└── README.md # Project documentation