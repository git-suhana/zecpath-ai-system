import re

COMMON_COMPLIANCE_SKILLS = [
    "aml",
    "kyc",
    "risk management",
    "regulatory compliance",
    "audit",
    "compliance monitoring",
    "policy analysis",
    "financial reporting",
    "internal controls",
    "fraud detection"
]


def extract_jd_skills(text):

    text = text.lower()

    found = []

    for skill in COMMON_COMPLIANCE_SKILLS:
        if skill in text:
            found.append(skill)

    return list(set(found))