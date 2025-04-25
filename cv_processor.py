import PyPDF2
from docx import Document

def extract_text(cv_path):
    if cv_path.endswith('.pdf'):
        with open(cv_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
    elif cv_path.endswith('.docx'):
        doc = Document(cv_path)
        text = "\n".join([para.text for para in doc.paragraphs])
    else:
        raise ValueError("Unsupported file format")
    return text