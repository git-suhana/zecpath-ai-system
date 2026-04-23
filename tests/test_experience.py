from parsers.pdf_reader import extract_text_from_pdf
from parsers.experience_parser import process_experience

pdf_path = "data/resumes/Resume_Suhana.pdf"

text = extract_text_from_pdf(pdf_path)

result = process_experience(text, "developer")

print(result)