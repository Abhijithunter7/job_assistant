# AI-Powered Job Assistant Tool

## Automatic Job Search Module with USAJOBS API

This module processes uploaded CVs, extracts key information, and matches them with job listings using the USAJOBS API.

### Setup

1. Install dependencies:
   ``` Python
   pip install -r requirements.txt
   ```
2. Request an API key
3. Replace `YOUR_API_KEY_HERE` in `job_matcher.py` with your  API key.
4. Run `main.py` with the path to your CV file.

### Usage

- Upload a CV in PDF or DOCX format.
- The script will extract text, identify skills/experiences, and fetch/rank job matches from the  API.

### Notes

- explore other APIs for broader coverage.
- Expand the `skill_keywords` and `experience_keywords` sets in `skill_extractor.py` for better accuracy.
- The similarity scoring in `job_matcher.py` is basic; consider using NLP techniques like TF-IDF for better results.
