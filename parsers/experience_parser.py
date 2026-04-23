
import re


#  STEP 1 — Extract experience blocks
def extract_experience_blocks(text):

    lines = [line.strip() for line in text.split("\n") if line.strip()]
    blocks = []

    for i, line in enumerate(lines):

        #  Skip bullets
        if line.startswith("•") or line.startswith("-"):
            continue

        #  Skip education & noise
        if any(word in line.lower() for word in [
            "university", "bachelor", "education", "@", "+91"
        ]):
            continue

        #  Detect date line
        if re.search(r"(20\d{2})", line):

            role = None
            company = None

            # Look upward for role & company
            for j in range(i - 1, max(i - 5, -1), -1):

                prev = lines[j]

                # skip bullets
                if prev.startswith("•") or prev.startswith("-"):
                    continue

                # detect role
                if not role and any(r in prev.lower() for r in [
                    "engineer", "developer", "analyst", "associate", "intern"
                ]):
                    role = prev
                    continue

                # next valid line → company
                if role and not company:
                    company = prev
                    break

            # build block
            block = ""

            if role:
                block += role + " "
            if company:
                block += company + " "

            block += line

            blocks.append(block.strip())

    return blocks


# STEP 2 — Parse block
def parse_experience_line(line):

    role = None
    company = None
    start_year = None
    end_year = None

    # ROLE detection
    roles = ["developer", "engineer", "analyst", "manager", "intern", "associate"]
    for r in roles:
        if r in line.lower():
            role = r
            break

    # YEAR extraction
    years = re.findall(r"(20\d{2})", line)

    if len(years) >= 2:
        start_year = int(years[0])
        end_year = int(years[1])
    elif len(years) == 1:
        start_year = int(years[0])
        end_year = int(years[0])

    # COMPANY extraction (safer)
    words = line.split()

    if words:
        for word in words:
            if (
                word.isalpha()
                and len(word) > 3
                and word.lower() not in roles
            ):
                company = word
                break

    return {
        "company": company,
        "role": role,
        "start_year": start_year,
        "end_year": end_year
    }


#  STEP 3 — Build structured experience
def build_experience_object(text):

    entries = extract_experience_blocks(text)

    print("FINAL BLOCKS:", entries)  # debug

    structured = []

    for entry in entries:
        structured.append(parse_experience_line(entry))

    return structured


#  STEP 4 — Total experience
def calculate_total_experience(experiences):

    total = 0

    for exp in experiences:
        if exp["start_year"] and exp["end_year"]:
            total += (exp["end_year"] - exp["start_year"])

    return total


#  STEP 5 — Detect gaps
def detect_gaps(experiences):

    sorted_exp = sorted(
        [exp for exp in experiences if exp["start_year"]],
        key=lambda x: x["start_year"]
    )

    gaps = []

    for i in range(len(sorted_exp) - 1):
        current_end = sorted_exp[i]["end_year"]
        next_start = sorted_exp[i + 1]["start_year"]

        if next_start - current_end > 1:
            gaps.append({
                "from": current_end,
                "to": next_start
            })

    return gaps


#  STEP 6 — Detect overlaps
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


#  STEP 7 — Relevance scoring
def relevance_score(experiences, job_role):

    score = 0
    job_role = job_role.lower()

    for exp in experiences:
        if exp["role"]:
            if job_role in exp["role"] or exp["role"] in job_role:
                score += 1

    if len(experiences) == 0:
        return 0

    return round(score / len(experiences), 2)


#  STEP 8 — Final pipeline
def process_experience(text, job_role):

    experiences = build_experience_object(text)

    return {
        "experience": experiences,
        "total_experience": calculate_total_experience(experiences),
        "gaps": detect_gaps(experiences),
        "overlaps": detect_overlaps(experiences),
        "relevance_score": relevance_score(experiences, job_role)
    }