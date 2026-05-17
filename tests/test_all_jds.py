import os
import json

from parsers.pdf_reader import extract_text_from_pdf
from parsers.skill_extraction_engine import skill_extraction_pipeline

from scoring.ats_matcher import (
    skill_match_score,
    classify_match
)


# =========================================================
# PATHS
# =========================================================

JD_FOLDER = "data/processed_jd"

RESUME_FOLDER = "data/resumes"


# =========================================================
# LOAD ALL JD FILES
# =========================================================

jd_files = [

    file for file in os.listdir(JD_FOLDER)

    if file.endswith(".json")
]


# =========================================================
# PROCESS EACH JD
# =========================================================

for jd_file in jd_files:

    print("\n\n=================================================")
    print(f"PROCESSING JD: {jd_file}")
    print("=================================================")

    jd_path = os.path.join(
        JD_FOLDER,
        jd_file
    )

    # -----------------------------------------------------
    # LOAD JD JSON
    # -----------------------------------------------------

    with open(jd_path, "r", encoding="utf-8") as file:

        jd_data = json.load(file)

    job_role = jd_data.get("job_role", "Unknown Role")

    jd_skills = jd_data.get(
        "required_skills",
        []
    )

    print(f"\nJOB ROLE: {job_role}")

    print(f"\nJD SKILLS: {jd_skills}")


    # =====================================================
    # STORE RESULTS
    # =====================================================

    results = []


    # =====================================================
    # CHECK ALL RESUMES
    # =====================================================

    for resume_file in os.listdir(RESUME_FOLDER):

        if not resume_file.endswith(".pdf"):
            continue

        resume_path = os.path.join(
            RESUME_FOLDER,
            resume_file
        )

        try:

            # -------------------------------------------------
            # EXTRACT RESUME TEXT
            # -------------------------------------------------

            resume_text = extract_text_from_pdf(
                resume_path
            )

            # -------------------------------------------------
            # EXTRACT SKILLS
            # -------------------------------------------------

            resume_result = skill_extraction_pipeline(
                resume_text
            )

            resume_skills = resume_result["skills"]

            # -------------------------------------------------
            # ATS MATCHING
            # -------------------------------------------------

            match_result = skill_match_score(
                jd_skills,
                resume_skills
            )

            score = match_result[
                "skill_match_score"
            ]

            classification = classify_match(
                score
            )

            # -------------------------------------------------
            # SAVE RESULT
            # -------------------------------------------------

            final_result = {

                "resume": resume_file,

                "score": score,

                "classification": classification,

                "matched_skills":
                    match_result["matched_skills"]
            }

            results.append(final_result)

        except Exception as e:

            print(f"\nERROR processing {resume_file}")
            print(e)


    # =====================================================
    # SORT RESULTS
    # =====================================================

    results = sorted(
        results,
        key=lambda x: x["score"],
        reverse=True
    )


    # =====================================================
    # SEPARATE MATCHING
    # =====================================================

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


    # =====================================================
    # PRINT MATCHING
    # =====================================================

    print("\n========== MATCHING RESUMES ==========")

    if len(matching_resumes) == 0:

        print("No matching resumes found.")

    else:

        for result in matching_resumes[:4]:

            print(result)


    # =====================================================
    # PRINT NON MATCHING
    # =====================================================

    print("\n========== NON-MATCHING RESUMES ==========")

    for result in non_matching_resumes[:4]:

        print(result)