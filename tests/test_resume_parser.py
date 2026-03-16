import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from parsers.resume_parser import parse_resume, save_cleaned_resume

resume_path = "data/resumes/Pranav.pdf"

text = parse_resume(resume_path)

save_cleaned_resume(text, "Pranav")

print("Resume processed and saved successfully!")

print("Extracted Text:\n")

print(text[:500])