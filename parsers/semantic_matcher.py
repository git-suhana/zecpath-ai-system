from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


# LOAD MODEL
model = SentenceTransformer('all-MiniLM-L6-v2')


# CREATE EMBEDDINGS
def create_embedding(text):

    embedding = model.encode(text)

    return embedding


# CALCULATE SIMILARITY
def semantic_similarity(resume_text, jd_text):

    resume_embedding = create_embedding(resume_text)

    jd_embedding = create_embedding(jd_text)

    similarity = cosine_similarity(
        [resume_embedding],
        [jd_embedding]
    )[0][0]

    return round(float(similarity), 2)


# CLASSIFICATION
def classify_similarity(score):

    if score >= 0.60:
        return "matching"

    elif score >= 0.40:
        return "partially matching"

    else:
        return "non-matching"


# FINAL PIPELINE
def semantic_match_resume(resume_text, jd_text):

    score = semantic_similarity(
        resume_text,
        jd_text
    )

    classification = classify_similarity(score)

    return {
        "semantic_score": score,
        "classification": classification
    }