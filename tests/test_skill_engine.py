from parsers.skill_extraction_engine import skill_extraction_pipeline
from parsers.pdf_reader import extract_text_from_pdf

pdf_path = "data/resumes/Resume_Suhana.pdf"

text = extract_text_from_pdf(pdf_path)

result = skill_extraction_pipeline(text)

print("\n===== SKILL EXTRACTION TEST =====")

print(result)