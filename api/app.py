from fastapi import FastAPI
import json

app = FastAPI()

# Load job listings from JSON file
def load_jobs():
    try:
        with open("api/jobs_data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@app.get("/jobs")
async def get_jobs(search: str = "", remote: bool = False):
    jobs = load_jobs()
    filtered_jobs = jobs
    
    # Filter by search term (case-insensitive)
    if search:
        search = search.lower()
        filtered_jobs = [
            job for job in filtered_jobs
            if search in job["title"].lower() or search in job["description"].lower()
        ]
    
    # Filter by remote
    if remote:
        filtered_jobs = [job for job in filtered_jobs if job["remote"]]
    
    return filtered_jobs