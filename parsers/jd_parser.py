import re
from parsers.jd_cleaner import clean_jd_text
from parsers.skill_extractor import extract_skills

def extract_experience(text):
    match = re.search(r"(\d+)\+?\s*years", text, re.IGNORECASE)
    if match:
        return match.group()
    return "Not specified"

def extract_education(text):
    if "bachelor" in text.lower():
        return "Bachelor's Degree"
    elif "master" in text.lower():
        return "Master's Degree"
    return "Not specified"

def extract_role(text):
    roles = [ "compliance officer",
        "compliance analyst",
        "compliance executive",
        "junior compliance officer",
        "senior compliance officer",
        "risk analyst",
        "audit officer"]
    for role in roles:
        if role in text.lower():
            return role
    return "Not specified"
def parse_job_description(raw_text):
    cleaned_text = clean_jd_text(raw_text)
    # Apply skill extraction + normalization 
    from parsers.skill_extractor import normalize_skills
    skills = extract_skills(cleaned_text)   # extract raw skills
    skills = normalize_skills(skills)  
    
    experience = extract_experience(cleaned_text)
    education = extract_education(cleaned_text)
    role = extract_role(cleaned_text)

    jd_object = {
        "job_role": role,
        "required_skills": skills,
        "experience_required": experience,
        "education_required": education
    }
    return jd_object


if __name__ == "__main__":
    sample_jd = """
    We are looking for a Python Developer with 3+ years experience.
    Candidate should have knowledge of Django, SQL and AWS.
    Bachelor's degree required.
    """

    result = parse_job_description(sample_jd)
    print(result)