import docx2txt
import fitz  # PyMuPDF

def extract_text(filepath):
    if filepath.endswith(".pdf"):
        doc = fitz.open(filepath)
        return "\n".join([page.get_text() for page in doc])
    elif filepath.endswith(".docx"):
        return docx2txt.process(filepath)
    else:
        return ""
