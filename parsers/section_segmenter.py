import re

SECTION_KEYWORDS = {
    "skills": ["skills", "technical skills", "core skills", "areas of expertise", "competencies"],
    "experience": ["experience", "work experience", "employment", "professional experience", "career history"],
    "education": ["education", "academic background", "qualifications", "academic history"],
    "projects": ["projects", "project work", "portfolio", "achievements"],
    "certifications": ["certifications", "certificates", "training", "achievements"]
}

GENERAL_KEYWORDS = {
    "skills": ["python", "java", "c++", "sql", "excel", "r", "data analysis", "machine learning", "tools", "visualization"],
    "experience": ["worked", "managed", "developed", "intern", "associate", "project", "led", "responsibilities", "collaborated"],
    "education": ["university", "college", "bachelor", "master", "degree", "school", "graduated", "diploma"],
    "projects": ["project", "portfolio", "developed", "built", "designed", "implemented", "created", "application", "system"],
    "certifications": ["certificate", "certifications", "certified", "training", "course", "achievement"]
}

def preprocess_text(text):
    lines = text.split("\n")
    clean_lines = []

    for line in lines:
        line = line.strip()
        if line:
            clean_lines.append(line)

    return "\n".join(clean_lines)

def classify_line(line):
    line_lower = line.lower()
    matches = {section: sum(1 for kw in keywords if kw in line_lower)
               for section, keywords in GENERAL_KEYWORDS.items()}
    best_section = max(matches, key=matches.get)
    if matches[best_section] > 0:
        return best_section
    return None

def detect_sections(text):
    sections = {key: "" for key in SECTION_KEYWORDS.keys()}
    current_section = None

    lines = text.split("\n")

    for line in lines:
        line = line.strip()
        if not line:
            continue

        line_lower = line.lower()

        #  STRONG heading detection
        for section, keywords in SECTION_KEYWORDS.items():
            if any(line_lower == kw or line_lower.startswith(kw) for kw in keywords):
                current_section = section
                break
        else:
            if current_section:
                sections[current_section] += line + " "
            else:
                predicted = classify_line(line)
                if predicted:
                    sections[predicted] += line + " "

    # Clean output
    for key in sections:
        sections[key] = sections[key].strip()

    return sections

def segment_resume(text):
    text = preprocess_text(text)
    return detect_sections(text)