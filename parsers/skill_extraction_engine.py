SKILL_DICTIONARY = {
    "programming": ["python", "java", "c++", "javascript"],
    "data": ["sql", "excel", "pandas", "numpy"],
    "ml": ["machine learning", "deep learning", "nlp"],
    "web": ["react", "node", "django", "flask"],
    "cloud": ["aws", "azure", "gcp"]
}
SKILL_SYNONYMS = {
    "ml": "machine learning",
    "ai": "artificial intelligence",
    "js": "javascript",
    "py": "python"
}
SKILL_STACKS = {
    "mern": ["mongodb", "express", "react", "node"],
    "mean": ["mongodb", "express", "angular", "node"]
}
def extract_skills(text):

    text = text.lower()
    found_skills = []

    # check dictionary
    for category, skills in SKILL_DICTIONARY.items():
        for skill in skills:
            if skill in text:
                found_skills.append(skill)

    # check stacks
    for stack, stack_skills in SKILL_STACKS.items():
        if stack in text:
            found_skills.extend(stack_skills)

    return found_skills
def normalize_skills(skills):

    normalized = []

    for skill in skills:
        if skill in SKILL_SYNONYMS:
            normalized.append(SKILL_SYNONYMS[skill])
        else:
            normalized.append(skill)

    return list(set(normalized))
def score_skills(text, skills):

    skill_scores = []

    for skill in skills:
        count = text.count(skill)

        if count >= 3:
            confidence = 0.9
        elif count == 2:
            confidence = 0.75
        else:
            confidence = 0.6

        skill_scores.append({
            "skill": skill,
            "confidence": confidence
        })

    return skill_scores
def skill_extraction_pipeline(text):

    extracted = extract_skills(text)
    normalized = normalize_skills(extracted)
    scored = score_skills(text, normalized)

    return scored