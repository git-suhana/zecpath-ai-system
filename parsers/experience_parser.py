import re
from datetime import datetime


# -----------------------------
# EXPERIENCE BLOCK EXTRACTION
# -----------------------------
def extract_experience_blocks(text):

    lines = [line.strip() for line in text.split("\n") if line.strip()]
    blocks = []

    for i, line in enumerate(lines):

        if re.search(r"(20\d{2})", line):

            role = None
            company = None

            for j in range(i - 1, max(i - 5, -1), -1):

                prev = lines[j].lower()

                role_keywords = [
                    "developer",
                    "engineer",
                    "analyst",
                    "manager",
                    "associate",
                    "intern",
                    "officer",
                    "executive"
                ]

                if not role:
                    for keyword in role_keywords:
                        if keyword in prev:
                            role = lines[j]
                            break

                elif not company:
                    company = lines[j]
                    break

            block = ""

            if role:
                block += role + " "

            if company:
                block += company + " "

            block += line

            blocks.append(block)

    return blocks


# -----------------------------
# PARSE SINGLE EXPERIENCE
# -----------------------------
def parse_experience_line(line):

    role = None
    company = None
    start_year = None
    end_year = None

    roles = [
        "developer",
        "engineer",
        "analyst",
        "manager",
        "associate",
        "intern",
        "officer",
        "executive"
    ]

    for r in roles:
        if r in line.lower():
            role = r
            break

    years = re.findall(r"(20\d{2})", line)

    if len(years) >= 2:
        start_year = int(years[0])
        end_year = int(years[1])

    elif len(years) == 1:
        start_year = int(years[0])
        end_year = datetime.now().year

    words = line.split()

    for word in words:
        if (
            word.isalpha()
            and len(word) > 3
            and word.lower() not in roles
        ):
            company = word
            break

    duration = 0

    if start_year and end_year:
        duration = end_year - start_year

    return {
        "company": company,
        "role": role,
        "start_year": start_year,
        "end_year": end_year,
        "duration": duration
    }


# -----------------------------
# BUILD EXPERIENCE OBJECT
# -----------------------------
def build_experience_object(text):

    blocks = extract_experience_blocks(text)

    experiences = []

    for block in blocks:
        experiences.append(parse_experience_line(block))

    return experiences


# -----------------------------
# TOTAL EXPERIENCE
# -----------------------------
def calculate_total_experience(experiences):

    if not experiences:
        return 0

    valid_years = []

    for exp in experiences:

        start = exp.get("start_year")
        end = exp.get("end_year")

        if start and end:

            # Avoid invalid years
            if start > end:
                continue

            # Avoid unrealistic ranges
            if end - start > 15:
                continue

            valid_years.append((start, end))

    if not valid_years:
        return 0

    # Find overall experience span
    earliest = min(start for start, end in valid_years)
    latest = max(end for start, end in valid_years)

    total_experience = latest - earliest

    if total_experience < 0:
        return 0

    return total_experience


# -----------------------------
# GAP DETECTION
# -----------------------------
def detect_gaps(experiences):

    gaps = []

    sorted_exp = sorted(
        experiences,
        key=lambda x: x["start_year"] if x["start_year"] else 0
    )

    for i in range(len(sorted_exp) - 1):

        current_end = sorted_exp[i]["end_year"]
        next_start = sorted_exp[i + 1]["start_year"]

        if current_end and next_start:

            if next_start - current_end > 1:

                gaps.append({
                    "from": current_end,
                    "to": next_start
                })

    return gaps


# -----------------------------
# OVERLAP DETECTION
# -----------------------------
def detect_overlaps(experiences):

    overlaps = []

    for i in range(len(experiences)):

        for j in range(i + 1, len(experiences)):

            a = experiences[i]
            b = experiences[j]

            if a["end_year"] and b["start_year"]:

                if a["end_year"] > b["start_year"]:

                    overlaps.append((a, b))

    return overlaps


# -----------------------------
# ROLE RELEVANCE
# -----------------------------
def relevance_score(experiences, job_role):

    if not job_role:
        return 0

    score = 0

    job_role = job_role.lower()

    for exp in experiences:

        if exp["role"]:

            if (
                exp["role"] in job_role
                or job_role in exp["role"]
            ):
                score += 1

    if len(experiences) == 0:
        return 0

    return round(score / len(experiences), 2)


# -----------------------------
# FINAL PIPELINE
# -----------------------------
def process_experience(text, job_role):

    experiences = build_experience_object(text)

    return {
        "experience": experiences,
        "total_experience": calculate_total_experience(experiences),
        "gaps": detect_gaps(experiences),
        "overlaps": detect_overlaps(experiences),
        "relevance_score": relevance_score(experiences, job_role)
    }