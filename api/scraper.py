import json
import os

def scrape_jobs():
    try:
        file_path = os.path.join(os.path.dirname(__file__), "jobs_data.json")
        print(f"Looking for file at: {file_path}")
        with open(file_path, "r") as f:
            jobs = json.load(f)
        return jobs
    except FileNotFoundError as e:
        print(f"jobs_data.json not found. Error: {e}. Returning empty list.")
        return []

if __name__ == "__main__":
    jobs = scrape_jobs()
    print(f"Loaded {len(jobs)} job listings.")