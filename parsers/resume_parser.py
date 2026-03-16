from parsers.pdf_reader import extract_text_from_pdf
from parsers.docx_reader import extract_text_from_docx
from parsers.text_cleaner import clean_resume_text


def parse_resume(file_path):

    if file_path.endswith(".pdf"):
        raw_text = extract_text_from_pdf(file_path)

    elif file_path.endswith(".docx"):
        raw_text = extract_text_from_docx(file_path)

    else:
        raise ValueError("Unsupported file format")

    clean_text = clean_resume_text(raw_text)

    return clean_text
def save_cleaned_resume(text, filename):

    output_path = f"data/processed_resumes/{filename}.txt"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)