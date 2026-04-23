from parsers.pdf_reader import extract_text_from_pdf
from parsers.education_parser import build_academic_profile

pdf_path = "data/resumes/Resume_Suhana.pdf"

text = extract_text_from_pdf(pdf_path)

job_role = "computer science"

result = build_academic_profile(text, job_role)

print("\n===== EDUCATION PARSER TEST =====")
print(f"Job Role: {job_role}")
print("Full Result:\n", result)