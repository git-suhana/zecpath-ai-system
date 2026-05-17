import json

from parsers.pdf_reader import extract_text_from_pdf
from parsers.skill_extraction_engine import skill_extraction_pipeline

from scoring.ats_matcher import (
    skill_match_score,
    classify_match
)


# =========================================================
# LOAD JD JSON
# =========================================================

with open("data/processed_jd/jd_1.json", "r", encoding="utf-8") as file:

    jd_data = json.load(file)

print("\n========== FULL JD JSON ==========")
print(jd_data)


# =========================================================
# GET JD SKILLS
# =========================================================

jd_skills = jd_data["required_skills"]

print("\n========== JD SKILLS ==========")
print(jd_skills)


# =========================================================
# LOAD RESUME
# =========================================================

resume_path = "data/resumes/Resume_Suhana.pdf"

resume_text = extract_text_from_pdf(resume_path)

resume_result = skill_extraction_pipeline(resume_text)

resume_skills = resume_result["skills"]

print("\n========== RESUME SKILLS ==========")
print(resume_skills)


# =========================================================
# ATS MATCHING
# =========================================================

match_result = skill_match_score(
    jd_skills,
    resume_skills
)

print("\n========== ATS MATCH RESULT ==========")
print(match_result)


# =========================================================
# CLASSIFICATION
# =========================================================

classification = classify_match(
    match_result["skill_match_score"]
)

print("\n========== CLASSIFICATION ==========")
print(classification)