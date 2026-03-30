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

