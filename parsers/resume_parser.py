import os
from parsers.pdf_reader import extract_text_from_pdf
from parsers.docx_reader import extract_text_from_docx
from parsers.text_cleaner import clean_resume_text, fix_broken_text

# OCR fallback
import pytesseract
from pdf2image import convert_from_path


def extract_text_ocr(file_path):
    text = ""
    pages = convert_from_path(file_path)

    for page in pages:
        text += pytesseract.image_to_string(page) + "\n"

    return text


def parse_resume(file_path):
    text = ""

    if file_path.lower().endswith(".pdf"):

        # ✅ STEP 1: Try PyMuPDF first
        print("📄 Trying PyMuPDF extraction...")
        text = extract_text_from_pdf(file_path)

        # ✅ DEBUG
        print("\n--- RAW TEXT (PyMuPDF) ---")
        print(text[:500])

        # ✅ STEP 2: If bad → fallback to OCR
        if len(text.strip()) < 100:
            print("⚠️ Falling back to OCR...")
            text = extract_text_ocr(file_path)

            print("\n--- OCR TEXT ---")
            print(text[:500])

    elif file_path.lower().endswith(".docx"):
        text = extract_text_from_docx(file_path)

    else:
        raise ValueError("Unsupported file format")

    # ✅ FIX broken OCR text
    text = fix_broken_text(text)

    # ✅ Clean but KEEP structure
    clean_text = clean_resume_text(text)

    return clean_text


def save_cleaned_resume(text, filename):
    output_path = f"data/processed_resumes/{filename}.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)