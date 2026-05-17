import fitz  # PyMuPDF
import pytesseract

from pdf2image import convert_from_path


# =========================================================
# PDF TEXT EXTRACTION + OCR FALLBACK
# =========================================================

def extract_text_from_pdf(file_path):

    text = ""

    # =====================================================
    # STEP 1 — NORMAL PDF EXTRACTION
    # =====================================================

    try:

        doc = fitz.open(file_path)

        for page in doc:

            text += page.get_text("text") + "\n"

        doc.close()

    except Exception as e:

        print(f"Error reading PDF: {e}")


    # =====================================================
    # STEP 2 — OCR FALLBACK
    # =====================================================

    # if extracted text is too small,
    # probably scanned/image resume

    if len(text.strip()) < 50:

        print(f"\nUsing OCR for: {file_path}")

        try:

            # OPTIONAL:
            # SET TESSERACT PATH (Windows)

            pytesseract.pytesseract.tesseract_cmd = (
                r"C:\Program Files\Tesseract-OCR\tesseract.exe"
            )

            images = convert_from_path(file_path)

            ocr_text = ""

            for image in images:

                extracted = pytesseract.image_to_string(image)

                ocr_text += extracted + "\n"

            text += ocr_text

        except Exception as e:

            print(f"OCR failed: {e}")

    return text