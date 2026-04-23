# Zecpath AI System

This repository contains AI modules for the Zecpath AI Job Portal.

Project structure:

data/ - datasets
parsers/ - resume parsing
ats_engine/ - ATS scoring
screening_ai/ - screening evaluation
interview_ai/ - interview evaluation
scoring/ - final candidate scoring
utils/ - utility modules
tests/ - testing scripts
logs/ - system logs


## Day 5 – Resume Extraction Engine

This module is the **first step in the AI pipeline**:

- Reads resumes in PDF and DOCX format
- Extracts raw text
- Cleans and normalizes text (removes special characters, extra spaces, inconsistent capitalization)
- Saves structured text outputs to `data/processed_resumes/`
- Can be tested with the automated script in `tests/test_resume_parser.py`


## Day 6 – Job Description Parsing System

**Objective:**  
Convert employer job descriptions into structured AI-readable objects.

**What was done:**  
- Extracted required skills, role names, experience, and education from job descriptions.  
- Cleaned and normalized JD text.  
- Handled skill synonyms and compliance-focused roles.  
- Built structured JSON outputs for all job descriptions.  

**Files included:**  
- `parsers/jd_parser.py` → Core parser module  
- `parsers/jd_cleaner.py` → JD text cleaning  
- `parsers/skill_extractor.py` → Skill extraction & normalization  
- `process_big_pdf_jds.py` → Runner script for single PDF with multiple JDs  
- `data/processed_jd/` → Sample JSON outputs  


 to run: `process_big_pdf_jds.py`


 ## Day 8- Resume Segmentation System
 This project implements a Resume Parsing and Section Segmentation system that processes resumes in PDF and DOCX formats and classifies content into structured sections.

## 🚀 Features
- Extracts text from:
  - PDF resumes (PyMuPDF)
  - DOCX resumes (python-docx)
- OCR fallback for scanned PDFs (Tesseract)
- Cleans and preprocesses text
- Segments resume into sections:
  - Skills
  - Experience
  - Education
  - Projects
  - Certifications
- Saves output as structured JSON

### Day 9 – Skill Extraction Engine

Objective
The objective of this task was to build a system capable of extracting relevant skills from resumes and structuring them for further use in job matching and candidate evaluation.

Implementation
A Skill Extraction Engine was developed to process unstructured resume text and identify both technical and non-technical skills. The system uses rule-based keyword matching along with a predefined skill dictionary to detect skills across multiple domains. It also includes synonym normalization to handle variations in naming (e.g., JS → JavaScript, AI → Artificial Intelligence) and expands grouped skill stacks such as MERN into individual technologies.
Each extracted skill is assigned a confidence score based on its frequency of occurrence in the resume, ensuring more prominent skills are given higher importance.

Key Features:
Extraction of technical and non-technical skills
Skill dictionary-based detection
Synonym normalization for consistency
Skill stack expansion (e.g., MERN)
Confidence scoring based on frequency
Structured skill output generation

Sample Output

[
  {"skill": "python", "confidence": 0.9},
  {"skill": "sql", "confidence": 0.75}
]

Challenges

Variations in skill naming conventions
Missing or unclear skill sections in resumes
Different resume formats and structures

## Day 10- Experience Parser

The experience parser extracts structured experience data from resume text.

It performs:
- Identification of experience sections using date patterns
- Extraction of role, company, and duration
- Filtering of irrelevant content (education, bullet points, contact info)

File:
parsers/experience_parser.py

###  Day 11 – Education & Certification Parsing

Extracts education details and certifications from resumes and evaluates their relevance to a job role.

Features
Extract degree, field, year, and institution
Identify and categorize certifications
Compute education relevance score (0–1)
Main Function
build_academic_profile(text, job_field)
Sample Output
{
  "education": [{"degree": "bachelor", "field": "computer science", "year": "2024"}],
  "institution": "University of Calicut, Kerala",
  "certifications": [{"name": "power bi", "category": "data"}],
  "education_relevance": 1.0
}
File:
parsers/education_parser.py
