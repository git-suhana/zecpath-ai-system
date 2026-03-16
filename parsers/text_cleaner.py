import re

def clean_resume_text(text):

    text = re.sub(r"[^\w\s]", " ", text)

    text = re.sub(r"\s+", " ", text)

    text = text.lower()

    return text.strip()