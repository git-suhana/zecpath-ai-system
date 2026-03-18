import os
import json
from parsers.jd_parser import parse_job_description

# Correct imports from your readers
from parsers.pdf_reader import extract_text_from_pdf
from parsers.docx_reader import extract_text_from_docx

# Folders
jd_folder = "data/Job_description"
processed_folder = "data/processed_jd"
os.makedirs(processed_folder, exist_ok=True)

# Loop through all JD files
for i, jd_file in enumerate(os.listdir(jd_folder), start=1):
    file_path = os.path.join(jd_folder, jd_file)
    ext = jd_file.lower().split('.')[-1]

    # Extract text based on file type
    if ext == "pdf":
        jd_text = extract_text_from_pdf(file_path)
    elif ext == "docx":
        jd_text = extract_text_from_docx(file_path)
    elif ext == "txt":
        with open(file_path, "r", encoding="utf-8") as f:
            jd_text = f.read()
    else:
        print(f"Skipping unsupported file type: {jd_file}")
        continue

    # Parse JD
    jd_obj = parse_job_description(jd_text)

    # Save JSON output
    out_file = os.path.join(processed_folder, f"jd_{i}.json")
    with open(out_file, "w", encoding="utf-8") as f_out:
        json.dump(jd_obj, f_out, indent=4)

    print(f"Processed {jd_file} → jd_{i}.json")  #progress output

print(f"All job descriptions processed. JSON files saved in {processed_folder}")