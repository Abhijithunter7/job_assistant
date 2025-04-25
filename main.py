import cv_processor
import skill_extractor
import job_matcher

def run_job_search(cv_path):
    # Step 1: Process the uploaded CV
    cv_text = cv_processor.extract_text(cv_path)
    
    # Step 2: Extract skills and keywords
    skills, experiences, keywords = skill_extractor.identify_key_elements(cv_text)
    
    # Step 3: Fetch and match jobs using GitHub Jobs API
    job_matches = job_matcher.fetch_and_rank_jobs(skills, experiences, keywords)
    
    return job_matches

if __name__ == "__main__":
    cv_path = "C:/Users/Admin/Documents/cv.pdf"  # Replace with actual CV path
    matches = run_job_search(cv_path)
    for match in matches:
        print(f"Job: {match['title']} - Score: {match['score']}%")