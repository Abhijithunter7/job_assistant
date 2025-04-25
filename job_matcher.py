<<<<<<< HEAD
import requests

def fetch_and_rank_jobs(skills, experiences, keywords):
    # Using your custom API
    api_url = "http://127.0.0.1:8000/jobs"
    params = {
        "search": ' '.join(skills + keywords),  # Combine skills and keywords for search
        "remote": "true" if "remote" in keywords else "false"
    }
    
    response = requests.get(api_url, params=params)
    jobs = response.json() if response.status_code == 200 else []
    
    # Similarity scoring based on job description and title
    matches = []
    for job in jobs:
        job_reqs = (job.get('title', '') + ' ' + job.get('description', '')).lower()
        req_tokens = set(job_reqs.split())
        cv_tokens = set(skills + experiences + keywords)
        score = min(len(req_tokens & cv_tokens) / len(req_tokens) * 100, 100) if req_tokens else 0
        matches.append({'title': job['title'], 'score': score})
    
=======
import requests

def fetch_and_rank_jobs(skills, experiences, keywords):
    # Using your custom API
    api_url = "http://127.0.0.1:8000/jobs"
    params = {
        "search": ' '.join(skills + keywords),  # Combine skills and keywords for search
        "remote": "true" if "remote" in keywords else "false"
    }
    
    response = requests.get(api_url, params=params)
    jobs = response.json() if response.status_code == 200 else []
    
    # Similarity scoring based on job description and title
    matches = []
    for job in jobs:
        job_reqs = (job.get('title', '') + ' ' + job.get('description', '')).lower()
        req_tokens = set(job_reqs.split())
        cv_tokens = set(skills + experiences + keywords)
        score = min(len(req_tokens & cv_tokens) / len(req_tokens) * 100, 100) if req_tokens else 0
        matches.append({'title': job['title'], 'score': score})
    
>>>>>>> b1a85c12968c793d8d17f1191b298263b60cd440
    return sorted(matches, key=lambda x: x['score'], reverse=True)