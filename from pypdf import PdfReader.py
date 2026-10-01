from pypdf import PdfReader
import os

def load_documents(folder):
    texts = []
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if file.endswith(".pdf"):
            reader = PdfReader(path)
            for page in reader.pages:
                texts.append(page.extract_text())
        elif file.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                texts.append(f.read())
    return texts
