import re


def extract_required_experience(experience_text):

    if not experience_text:
        return 0

    match = re.search(r"(\d+)", experience_text)

    if match:
        return int(match.group(1))

    return 0


def match_experience(jd_experience, resume_total_experience):

    required_years = extract_required_experience(jd_experience)

    if required_years == 0:
        return {
            "required_experience": 0,
            "resume_experience": resume_total_experience,
            "experience_score": 0,
            "classification": "non-matching"
        }

    score = resume_total_experience / required_years

    if score > 1:
        score = 1

    if score >= 0.7:
        classification = "matching"

    elif score >= 0.4:
        classification = "partially matching"

    else:
        classification = "non-matching"

    return {
        "required_experience": required_years,
        "resume_experience": resume_total_experience,
        "experience_score": round(score, 2),
        "classification": classification
    }