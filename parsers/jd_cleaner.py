import re

def clean_jd_text(text):
    """
    Cleans job description text for easier parsing
    """

    # 1. Convert to lowercase
    text = text.lower()

    # 2. Remove special characters (keep only words & spaces)
    text = re.sub(r"[^\w\s]", " ", text)

    # 3. Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()

if __name__ == "__main__":
    sample = "Looking for Python Developer!!! 3+ years experience."
    print(clean_jd_text(sample))