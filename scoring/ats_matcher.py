# =========================================================
# ATS MATCHER ENGINE
# =========================================================


# =========================================================
# NORMALIZE SKILLS
# =========================================================

SKILL_NORMALIZATION = {

    "ms excel": "excel",
    "microsoft excel": "excel",

    "powerbi": "power bi",

    "anti money laundering": "aml",
    "know your customer": "kyc"
}


def normalize_skill(skill):

    skill = skill.lower().strip()

    return SKILL_NORMALIZATION.get(skill, skill)


# =========================================================
# EXTRACT RESUME SKILL NAMES
# =========================================================

def get_resume_skill_names(resume_skills):

    return [

        normalize_skill(skill["skill"])

        for skill in resume_skills
    ]


# =========================================================
# MATCH JD VS RESUME SKILLS
# =========================================================

def skill_match_score(jd_skills, resume_skills):

    matched_skills = []

    normalized_jd_skills = [

        normalize_skill(skill)

        for skill in jd_skills
    ]

    normalized_resume_skills = get_resume_skill_names(
        resume_skills
    )

    for jd_skill in normalized_jd_skills:

        if jd_skill in normalized_resume_skills:

            matched_skills.append(jd_skill)

    # avoid division error
    if len(jd_skills) == 0:

        score = 0

    else:

        score = len(matched_skills) / len(jd_skills)

    return {

        "matched_skills": matched_skills,

        "matched_count": len(matched_skills),

        "total_jd_skills": len(jd_skills),

        "skill_match_score": round(score, 2)
    }


# =========================================================
# CLASSIFY MATCH
# =========================================================

def classify_match(score):

    if score >= 0.50:
        return "matching"

    elif score >= 0.20:
        return "partially matching"

    else:
        return "non-matching"