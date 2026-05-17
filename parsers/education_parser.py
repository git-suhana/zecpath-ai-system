import re


DEGREES = [
    "b.tech",
    "bachelor",
    "m.tech",
    "master",
    "mba",
    "phd",
    "bcom",
    "mcom"
]


FIELDS = [
    "computer science",
    "information technology",
    "electronics",
    "business administration",
    "data science",
    "accounting",
    "financial management",
    "commerce",
    "finance"
]


CERTIFICATIONS = [
    "aws",
    "azure",
    "google cloud",
    "pmp",
    "scrum",
    "data analyst",
    "power bi",
    "aml",
    "kyc",
    "compliance"
]


CERT_CATEGORIES = {
    "aws": "cloud",
    "azure": "cloud",
    "google cloud": "cloud",
    "pmp": "management",
    "scrum": "management",
    "data analyst": "data",
    "power bi": "data",
    "aml": "compliance",
    "kyc": "compliance",
    "compliance": "compliance"
}


# -----------------------------
# EDUCATION EXTRACTION
# -----------------------------
def extract_education(text):

    text = text.lower()

    education = []

    for degree in DEGREES:

        if degree in text:

            field_found = None

            for field in FIELDS:

                if field in text:
                    field_found = field
                    break

            year_match = re.search(r"\b(20\d{2}|19\d{2})\b", text)

            year = year_match.group() if year_match else None

            education.append({
                "degree": degree,
                "field": field_found,
                "graduation_year": year
            })

    return education


# -----------------------------
# INSTITUTION EXTRACTION
# -----------------------------
def extract_institution(text):

    lines = text.split("\n")

    institutions = []

    for line in lines:

        lower = line.lower()

        if (
            "university" in lower
            or "college" in lower
            or "institute" in lower
        ):
            institutions.append(line.strip())

    return list(set(institutions))


# -----------------------------
# CERTIFICATION EXTRACTION
# -----------------------------
def extract_certifications(text):

    text = text.lower()

    found = []

    for cert in CERTIFICATIONS:

        if cert in text:
            found.append(cert)

    return list(set(found))


# -----------------------------
# CERTIFICATION CATEGORIZATION
# -----------------------------
def categorize_certifications(certs):

    categorized = []

    for cert in certs:

        category = CERT_CATEGORIES.get(cert, "other")

        categorized.append({
            "name": cert,
            "category": category
        })

    return categorized


# -----------------------------
# EDUCATION RELEVANCE
# -----------------------------
def education_relevance(education, job_field):

    if not job_field:
        return 0

    score = 0

    job_field = job_field.lower()

    for edu in education:

        if edu["field"]:

            if (
                job_field in edu["field"]
                or edu["field"] in job_field
            ):
                score += 1

    if len(education) == 0:
        return 0

    return round(score / len(education), 2)


# -----------------------------
# FINAL PIPELINE
# -----------------------------
def build_academic_profile(text, job_field):

    education = extract_education(text)

    institutions = extract_institution(text)

    certs = extract_certifications(text)

    categorized_certs = categorize_certifications(certs)

    relevance = education_relevance(
        education,
        job_field
    )

    return {
        "education": education,
        "institutions": institutions,
        "certifications": categorized_certs,
        "education_relevance": relevance
    }