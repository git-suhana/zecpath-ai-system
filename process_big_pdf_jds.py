# process_big_pdf_jds.py
import os
import json
import re
from parsers.jd_parser import parse_job_description
from parsers.pdf_reader import extract_text_from_pdf

# PDF containing all JDs
big_pdf_file = "data/Job_description/Compliance Officer Models.pdf"
processed_folder = "data/processed_jd"
os.makedirs(processed_folder, exist_ok=True)

# Step 1: Extract entire text from PDF
try:
    full_text = extract_text_from_pdf(big_pdf_file)
except Exception as e:
    print(f"Error reading PDF: {e}")
    exit()

# Step 2: Split text into individual JDs
# Pattern: number at start of line followed by period (handles possible Unicode variants)
jd_blocks = re.split(r'\n\d+[\uFE0F]?\.\s', full_text)
jd_blocks = [block.strip() for block in jd_blocks if block.strip()]

total_jds = len(jd_blocks)
print(f"Total JDs found in PDF: {total_jds}\n")

# Step 3: Parse each JD and save JSON
for i, jd_text in enumerate(jd_blocks, start=1):
    jd_obj = parse_job_description(jd_text)

    # Save JSON
    out_file = os.path.join(processed_folder, f"jd_{i}.json")
    with open(out_file, "w", encoding="utf-8") as f_out:
        json.dump(jd_obj, f_out, indent=4)

    # Print summary
    print(f"{i}/{total_jds} → jd_{i}.json")
    print(f"   Role: {jd_obj['job_role']}, Skills: {jd_obj['required_skills']}, "
          f"Experience: {jd_obj['experience_required']}, Education: {jd_obj['education_required']}\n")

print(f"All {total_jds} job descriptions processed. JSON files saved in {processed_folder}")