from parsers.skill_extraction_engine import skill_extraction_pipeline
from parsers.resume_parser import parse_resume

resume_path = "data/resumes/Pranav.pdf"

text = parse_resume(resume_path)

skills = skill_extraction_pipeline(text)

for skill in skills:
    print(skill)