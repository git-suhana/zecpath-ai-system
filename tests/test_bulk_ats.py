import os
import json

from parsers.pdf_reader import extract_text_from_pdf
from parsers.skill_extraction_engine import skill_extraction_pipeline

from scoring.ats_matcher import (
    skill_match_score,
    classify_match
)


# =========================================================
# LOAD ONE JD
# =========================================================

with open(
    "data/processed_jd/jd_1.json",
    "r",
    encoding="utf-8"
) as file:

    jd_data = json.load(file)

jd_skills = jd_data["required_skills"]

print("\n========== JD ==========")
print(jd_data["job_role"])

print("\n========== JD SKILLS ==========")
print(jd_skills)


# =========================================================
# LOAD ALL RESUMES
# =========================================================

resume_folder = "data/resumes"

results = []


# =========================================================
# PROCESS EACH RESUME
# =========================================================

for resume_file in os.listdir(resume_folder):

    # only PDFs
    if not resume_file.endswith(".pdf"):
        continue

    resume_path = os.path.join(
        resume_folder,
        resume_file
    )

    try:

        # extract text
        resume_text = extract_text_from_pdf(
            resume_path
        )

        # extract resume skills
        resume_result = skill_extraction_pipeline(
            resume_text
        )

        resume_skills = resume_result["skills"]

        # ATS matching
        match_result = skill_match_score(
            jd_skills,
            resume_skills
        )

        classification = classify_match(
            match_result["skill_match_score"]
        )

        final_result = {

            "resume": resume_file,

            "score": match_result["skill_match_score"],

            "classification": classification,

            "matched_skills":
                match_result["matched_skills"]
        }

        results.append(final_result)

    except Exception as e:

        print(f"\nERROR processing {resume_file}")
        print(e)


# =========================================================
# SORT RESULTS
# =========================================================

results = sorted(
    results,
    key=lambda x: x["score"],
    reverse=True
)


# =========================================================
# SEPARATE MATCHING & NON-MATCHING
# =========================================================

matching_resumes = []
non_matching_resumes = []

for result in results:

    if result["classification"] in [
        "matching",
        "partially matching"
    ]:

        matching_resumes.append(result)

    else:

        non_matching_resumes.append(result)


# =========================================================
# PRINT MATCHING RESUMES
# =========================================================

print("\n\n========== MATCHING RESUMES ==========")

if len(matching_resumes) == 0:

    print("No matching resumes found.")

else:

    for result in matching_resumes[:4]:
        print(result)


# =========================================================
# PRINT NON-MATCHING RESUMES
# =========================================================

print("\n\n========== NON-MATCHING RESUMES ==========")

for result in non_matching_resumes[:4]:
    print(result)