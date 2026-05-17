import os
import json

from parsers.pdf_reader import extract_text_from_pdf
from parsers.experience_parser import process_experience
from scoring.experience_matcher import match_experience


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
    experience_required = jd_data.get("experience_required", "0 years")

    print(f"\nJOB ROLE: {job_role}")
    print(f"REQUIRED EXPERIENCE: {experience_required}")

    matching = []
    non_matching = []

    for resume_file in os.listdir(resume_folder):

        if not resume_file.endswith(".pdf"):
            continue

        resume_path = os.path.join(resume_folder, resume_file)

        text = extract_text_from_pdf(resume_path)

        result = process_experience(text, job_role)

        total_exp = result["total_experience"]

        match_result = match_experience(
            experience_required,
            total_exp
        )

        final_result = {
            "resume": resume_file,
            "total_experience": total_exp,
            "score": match_result["experience_score"],
            "classification": match_result["classification"]
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