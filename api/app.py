from fastapi import FastAPI, Query
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from scraper import scrape_jobs
from typing import List, Optional

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (adjust for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load job listings using scraper.py
def load_jobs():
    return scrape_jobs()

@app.get("/")
async def root():
    return RedirectResponse(url="/jobs")

@app.get("/jobs")
async def get_jobs(
    job_title: Optional[str] = Query(None, description="Filter by job title"),
    location: Optional[str] = Query(None, description="Filter by location"),
    company: Optional[str] = Query(None, description="Filter by company"),
    skills: Optional[str] = Query(None, description="Filter by skills (comma separated)"),
    keywords: Optional[str] = Query(None, description="Filter by keywords (comma separated)"),
    remote: bool = Query(False, description="Filter by remote jobs")
):
    jobs = load_jobs()
    filtered_jobs = jobs

    if job_title:
        filtered_jobs = [job for job in filtered_jobs if job_title.lower() in job["title"].lower()]

    if location:
        filtered_jobs = [job for job in filtered_jobs if location.lower() in job["location"].lower()]

    if company:
        filtered_jobs = [job for job in filtered_jobs if company.lower() in job["company"].lower()]

    if skills:
        skill_list = skills.lower().split(',')
        filtered_jobs = [job for job in filtered_jobs if all(skill.strip() in (job["description"].lower() + job["title"].lower()) for skill in skill_list)]

    if keywords:
        keyword_list = keywords.lower().split(',')
        filtered_jobs = [job for job in filtered_jobs if all(keyword.strip() in (job["description"].lower() + job["title"].lower()) for keyword in keyword_list)]

    if remote:
        filtered_jobs = [job for job in filtered_jobs if job["remote"]]

    return filtered_jobs