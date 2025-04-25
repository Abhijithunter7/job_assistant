import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

# Download required NLTK data (run once)
nltk.download('punkt')
nltk.download('stopwords')

def identify_key_elements(text):
    # Tokenization and cleaning
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english') + list(string.punctuation))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    # Predefined skill and keyword lists (tech-focused for GitHub Jobs API)
    skill_keywords = {'python', 'javascript', 'java', 'sql', 'ruby', 'react', 'node', 'aws'}
    experience_keywords = {'years', 'experience', 'project', 'lead', 'developed', 'engineer'}
    
    skills = [skill for skill in filtered_tokens if skill in skill_keywords]
    experiences = [exp for exp in filtered_tokens if exp in experience_keywords]
    keywords = set(filtered_tokens) - skill_keywords - experience_keywords
    
    return skills, experiences, list(keywords)