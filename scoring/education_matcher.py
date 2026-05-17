def match_education(education_relevance, certifications):

    cert_score = 0

    if len(certifications) >= 3:
        cert_score = 0.4

    elif len(certifications) >= 1:
        cert_score = 0.2

    final_score = education_relevance + cert_score

    if final_score > 1:
        final_score = 1

    if final_score >= 0.7:
        classification = "matching"

    elif final_score >= 0.4:
        classification = "partially matching"

    else:
        classification = "non-matching"

    return {
        "education_score": round(final_score, 2),
        "classification": classification
    }