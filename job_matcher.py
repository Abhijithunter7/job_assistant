import requests

def fetch_and_rank_jobs(skills, experiences, keywords):
    # Using API
    api_url = "YOUR API KEY"
    params = {
        'description': ' '.join(skills + keywords),  # Combine skills and keywords for search
        'location': 'remote' if 'remote' in keywords else '',
        'full_time': 'true'
    }
    
    response = requests.get(api_url, params=params)
    jobs = response.json() if response.status_code == 200 else []
    
    # Similarity scoring based on job description and title
    matches = []
    for job in jobs:
        job_reqs = (job.get('description', '') + ' ' + job.get('title', '')).lower()
        req_tokens = set(job_reqs.split())
        cv_tokens = set(skills + experiences + keywords)
        score = min(len(req_tokens & cv_tokens) / len(req_tokens) * 100, 100) if req_tokens else 0
        matches.append({'title': job['title'], 'score': score})
    
    return sorted(matches, key=lambda x: x['score'], reverse=True)
