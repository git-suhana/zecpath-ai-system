import os
import json
from parsers.resume_parser import parse_resume
from parsers.section_segmenter import segment_resume

RESUME_FOLDER = "data/resumes"
OUTPUT_FOLDER = "data/segmented_resumes"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for file in os.listdir(RESUME_FOLDER):
    if file.lower().endswith((".pdf", ".docx")):
        print(f"\nProcessing: {file}")
        resume_path = os.path.join(RESUME_FOLDER, file)
        text = parse_resume(resume_path)
        sections = segment_resume(text)

        # Print a preview
        for section, content in sections.items():
            print(f"\n--- {section.upper()} ---")
            print(content[:300])  # first 300 chars

        # Save JSON
        base_name = os.path.splitext(file)[0]
        output_path = os.path.join(OUTPUT_FOLDER, f"{base_name}.json")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(sections, f, indent=4)
        print(f"Saved segmented JSON: {output_path}")

        print("\n===== FINAL CLEAN TEXT =====\n")
        print(text[:1000])