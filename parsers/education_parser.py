DEGREES = ["b.tech", "bachelor", "m.tech", "master", "mba", "phd"]

FIELDS = [
    "computer science",
    "information technology",
    "electronics",
    "business administration",
    "data science"
    "accounting"
    "financial management"
]

CERTIFICATIONS = [
    "aws", "azure", "google cloud",
    "pmp", "scrum", "data analyst","power bi",
]
import re

def extract_education(text):

    text = text.lower()
    education = []

    for degree in DEGREES:
        if degree in text:

            field_found = None
            for field in FIELDS:
                if field in text:
                    field_found = field

            year_match = re.search(r"\b(20\d{2}|19\d{2})\b", text)
            year = year_match.group() if year_match else None

            education.append({
                "degree": degree,
                "field": field_found,
                "year": year
            })

    return education
def extract_institution(text):

    lines = text.split("\n")

    for line in lines:
        if "university" in line.lower() or "college" in line.lower():
            return line.strip()

    return "Not specified"
def extract_certifications(text):

    text = text.lower()
    found = []

    for cert in CERTIFICATIONS:
        if cert in text:
            found.append(cert)

    return list(set(found))
CERT_CATEGORIES = {
    "aws": "cloud",
    "azure": "cloud",
    "google cloud": "cloud",
    "pmp": "management",
    "scrum": "management",
    "data analyst": "data"
 
    
}

def categorize_certifications(certs):

    result = []

    for cert in certs:
        category = CERT_CATEGORIES.get(cert, "other")

        result.append({
            "name": cert,
            "category": category
        })

    return result
def education_relevance(education, job_field):

    score = 0

    for edu in education:
        if edu["field"] and job_field.lower() in edu["field"]:
            score += 1

    if len(education) == 0:
        return 0

    return round(score / len(education), 2)
def build_academic_profile(text, job_field):

    education = extract_education(text)
    institution = extract_institution(text)
    certs = extract_certifications(text)
    categorized_certs = categorize_certifications(certs)

    relevance = education_relevance(education, job_field)

    return {
        "education": education,
        "institution": institution,
        "certifications": categorized_certs,
        "education_relevance": relevance
    }