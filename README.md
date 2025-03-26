# ATS Resume Expert System

## Overview
An AI-powered Applicant Tracking System (ATS) analyzer that evaluates resumes against job descriptions using Google's Gemini AI. Provides professional evaluations, skill gap analysis, and match percentage calculations.

## Features
- Resume evaluation against job descriptions
- Skill gap identification and improvement suggestions
- Percentage match scoring
- Strengths/weaknesses analysis
- AI-powered insights from Gemini-2.0-Flash model

## Installation
1. Clone repository:
```bash
git clone [your-repository-url]
```
2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Requirements
Create `requirements.txt` with:
```
streamlit
python-dotenv
google-generativeai
pdf2image
pillow
```

## Configuration
1. Get Google API key from [Google AI Studio](https://aistudio.google.com/)
2. Create `.env` file:
```env
GOOGLE_API_KEY=your_api_key_here
```

## Poppler Setup (Required for PDF processing)
- Windows: Download from [poppler-for-windows](https://github.com/oschwartz10612/poppler-windows/releases/) and update path in `app.py`
- Linux:
```bash
sudo apt-get install poppler-utils
```
- Mac:
```bash
brew install poppler
```

## Usage
```bash
streamlit run app.py
```

1. Enter job description in text area
2. Upload PDF resume
3. Use buttons to:
   - Get resume evaluation
   - Receive skill improvement suggestions
   - Calculate percentage match

## Technologies
- Google Gemini AI 2.0 Flash (You can select from list of available models from google)
- Streamlit (Web Interface)
- PDF2Image (PDF processing)
- Poppler (PDF rendering)


## Contributing
Contributions welcome! Please open an issue first to discuss proposed changes.

## Acknowledgments
- Google Gemini API
- Streamlit team
- PDF2Image/Poppler maintainers
