import re


# =========================================================
# MASTER SKILL DICTIONARY
# =========================================================

MASTER_SKILLS = [

    # Compliance
    "aml",
    "kyc",
    "regulatory compliance",
    "risk management",
    "compliance monitoring",
    "fraud detection",
    "internal controls",
    "audit",
    "policy analysis",
    "compliance reporting",

    # Finance
    "financial reporting",
    "financial analysis",
    "accounting",
    "taxation",

    # Business
    "communication",
    "documentation",
    "team management",
    "problem solving",

    # Tools
    "excel",
    "power bi",
    "sap"
    "attention to detail",
    "documentation",
    "compliance",
    "policy drafting",
    "regulatory knowledge",
    "securities and exchange board of india",
    "reserve bank of india"
    "regulatory compliance",
    "legal compliance",
    "governance",
    "risk analysis",
    "risk assessment",
    "ethics",
    "internal audit",
    "financial audit",
    "investigation",
    "compliance review",
    "compliance operations",
    "reporting",
    "legal documentation",
    "compliance framework",
    "banking regulations",
    "data privacy",
    "gdpr",
    "corporate compliance",
    "financial crime",
    "sar filing"
]


# =========================================================
# SKILL SYNONYMS
# =========================================================

SKILL_SYNONYMS = {

    "anti money laundering": "aml",
    "know your customer": "kyc",

    "ms excel": "excel",
    "microsoft excel": "excel",

    "powerbi": "power bi",

    "risk assessment": "risk management",
    "compliance checks": "compliance monitoring"
}


# =========================================================
# TEXT CLEANING
# =========================================================

def clean_text(text):

    text = text.lower()

    # remove special characters
    text = re.sub(r"[^\w\s]", " ", text)

    # remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# =========================================================
# EXTRACT SKILLS
# =========================================================

def extract_skills(text):

    text = clean_text(text)

    found_skills = []

    # direct skill matching
    for skill in MASTER_SKILLS:

        if skill in text:
            found_skills.append(skill)

    # synonym matching
    for synonym, actual_skill in SKILL_SYNONYMS.items():

        if synonym in text:
            found_skills.append(actual_skill)

    return list(set(found_skills))


# =========================================================
# NORMALIZE SKILLS
# =========================================================

def normalize_skills(skills):

    normalized = []

    for skill in skills:

        skill = skill.lower().strip()

        if skill in SKILL_SYNONYMS:
            normalized.append(SKILL_SYNONYMS[skill])

        else:
            normalized.append(skill)

    return list(set(normalized))


# =========================================================
# CONFIDENCE SCORING
# =========================================================

def score_skills(text, skills):

    text = clean_text(text)

    scored_skills = []

    for skill in skills:

        count = text.count(skill)

        # confidence logic
        if count >= 3:
            confidence = 0.95

        elif count == 2:
            confidence = 0.80

        else:
            confidence = 0.60

        scored_skills.append({

            "skill": skill,
            "confidence": confidence
        })

    return scored_skills


# =========================================================
# FINAL SKILL PIPELINE
# =========================================================

def skill_extraction_pipeline(text):

    extracted = extract_skills(text)

    normalized = normalize_skills(extracted)

    scored = score_skills(text, normalized)

    return {

        "skills": scored,

        "total_skills_found": len(scored)
    }