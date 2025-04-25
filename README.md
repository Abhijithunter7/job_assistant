AI-Powered Job Assistant Tool
Automatic Job Search Module with GitHub Jobs API
This module processes uploaded CVs, extracts key information, and matches them with job listings using the GitHub Jobs API.
Setup

Install dependencies:pip install -r requirements.txt


Run main.py with the path to your CV file.

Usage

Upload a CV in PDF or DOCX format.
The script will extract text, identify skills/experiences, and fetch/rank job matches from GitHub Jobs API.

Notes

The GitHub Jobs API is used (https://jobs.github.com/positions.json).
Expand the skill_keywords and experience_keywords sets in skill_extractor.py for better accuracy.
The similarity scoring in job_matcher.py is basic; consider using NLP techniques like TF-IDF for better results.

