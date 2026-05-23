import os
import json

from parsers.pdf_reader import extract_text_from_pdf
from parsers.semantic_matcher import semantic_match_resume


JD_FOLDER = "data/processed_jd"
RESUME_FOLDER = "data/resumes"


# LOOP THROUGH ALL JDs
for jd_file in os.listdir(JD_FOLDER):

    if not jd_file.endswith(".json"):
        continue

    print("\n=================================================")
    print(f"PROCESSING JD: {jd_file}")
    print("=================================================")

    # LOAD JD
    jd_path = os.path.join(JD_FOLDER, jd_file)

    with open(jd_path, "r", encoding="utf-8") as f:
        jd_data = json.load(f)

    job_role = jd_data.get("job_role", "Not specified")

    jd_skills = jd_data.get("required_skills", [])

    jd_text = job_role + " " + " ".join(jd_skills)

    print(f"\nJOB ROLE: {job_role}")

    matching_resumes = []
    non_matching_resumes = []

    # LOOP THROUGH RESUMES
    for resume_file in os.listdir(RESUME_FOLDER):

        if not resume_file.endswith(".pdf"):
            continue

        resume_path = os.path.join(
            RESUME_FOLDER,
            resume_file
        )

        resume_text = extract_text_from_pdf(
            resume_path
        )

        result = semantic_match_resume(
            resume_text,
            jd_text
        )

        output = {
            "resume": resume_file,
            "semantic_score": result["semantic_score"],
            "classification": result["classification"]
        }

        if result["classification"] == "matching":
            matching_resumes.append(output)

        else:
            non_matching_resumes.append(output)

    # SORT RESULTS
    matching_resumes = sorted(
        matching_resumes,
        key=lambda x: x["semantic_score"],
        reverse=True
    )

    non_matching_resumes = sorted(
        non_matching_resumes,
        key=lambda x: x["semantic_score"],
        reverse=True
    )

    print("\n========== MATCHING RESUMES ==========")

    if matching_resumes:
        for r in matching_resumes[:5]:
            print(r)

    else:
        print("No matching resumes found.")

    print("\n========== NON-MATCHING RESUMES ==========")

    for r in non_matching_resumes[:5]:
        print(r)