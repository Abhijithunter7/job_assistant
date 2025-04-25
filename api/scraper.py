import json
import requests
from bs4 import BeautifulSoup

def scrape_jobs():
    # Mock job listings (replace with actual scraping logic)
    jobs = [
        {
            "title": "Machine Learning Engineer",
            "company": "TechIndia Solutions",
            "description": "Develop machine learning models using Python and TensorFlow. 3+ years experience required.",
            "location": "Bangalore",
            "remote": False
        },
        {
            "title": "Data Scientist",
            "company": "DataCorp India",
            "description": "Analyze large datasets with SQL and Python. Experience with AWS preferred.",
            "location": "Mumbai",
            "remote": True
        },
        {
            "title": "Software Engineer",
            "company": "InnovateTech",
            "description": "Build scalable applications using Java and React. 2 years experience needed.",
            "location": "Hyderabad",
            "remote": False
        },
        {
            "title": "Product Designer",
            "company": "DesignWorks",
            "description": "Design user interfaces for web applications. Proficiency in Figma required.",
            "location": "Delhi",
            "remote": True
        }
    ]
    
    # Save to JSON file
    with open("api/jobs_data.json", "w") as f:
        json.dump(jobs, f)

if __name__ == "__main__":
    scrape_jobs()