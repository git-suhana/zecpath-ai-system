import os
import json

from parsers.pdf_reader import extract_text_from_pdf
from parsers.education_parser import build_academic_profile
from scoring.education_matcher import match_education


jd_folder = "data/processed_jd"
resume_folder = "data/resumes"


for jd_file in os.listdir(jd_folder):

    if not jd_file.endswith(".json"):
        continue

    print("\n=================================================")
    print(f"PROCESSING JD: {jd_file}")
    print("=================================================")

    jd_path = os.path.join(jd_folder, jd_file)

    with open(jd_path, "r", encoding="utf-8") as file:
        jd_data = json.load(file)

    job_role = jd_data.get("job_role", "Not specified")

    print(f"\nJOB ROLE: {job_role}")

    matching = []
    non_matching = []

    for resume_file in os.listdir(resume_folder):

        if not resume_file.endswith(".pdf"):
            continue

        resume_path = os.path.join(
            resume_folder,
            resume_file
        )

        text = extract_text_from_pdf(resume_path)

        result = build_academic_profile(
            text,
            job_role
        )

        match_result = match_education(
            result["education_relevance"],
            result["certifications"]
        )

        final_result = {
            "resume": resume_file,
            "education_score": match_result["education_score"],
            "classification": match_result["classification"],
            "certifications": result["certifications"]
        }

        if match_result["classification"] == "matching":
            matching.append(final_result)

        else:
            non_matching.append(final_result)

    print("\n========== MATCHING RESUMES ==========")

    if matching:
        for item in matching[:4]:
            print(item)

    else:
        print("No matching resumes found.")

    print("\n========== NON-MATCHING RESUMES ==========")

    for item in non_matching[:4]:
        print(item)