COMMON_SKILLS = [
    "compliance",
    "risk assessment",
    "aml",
    "kyc",
    "fraud detection",
    "audit",
    "reporting",
    "documentation",
    "regulatory knowledge",
    "policy drafting",
    "ms excel",
    "analytical thinking",
    "attention to detail",
    "rbi",
    "sebi"
]
def extract_skills(text):
    """
    Extract skills from cleaned job description
    """

    found_skills = []

    for skill in COMMON_SKILLS:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))  # remove duplicates

SKILL_SYNONYMS = {
   "aml": "anti-money laundering",
    "kyc": "know your customer",
    "rbi": "reserve bank of india",
    "sebi": "securities and exchange board of india"
}
def normalize_skills(skills):

    normalized = []

    for skill in skills:
        if skill in SKILL_SYNONYMS:
            normalized.append(SKILL_SYNONYMS[skill])
        else:
            normalized.append(skill)

    return list(set(normalized))
if __name__ == "__main__":

    sample_text = "Looking for ML engineer with Python and JS skills"

    from parsers.jd_cleaner import clean_jd_text

    cleaned = clean_jd_text(sample_text)

    skills = extract_skills(cleaned)
    skills = normalize_skills(skills)

    print(skills)