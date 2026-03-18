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
