import re

def clean_resume_text(text):

    # Keep line breaks!
    text = re.sub(r"[^\w\s\n]", " ", text)

    # Normalize spaces (but NOT newlines)
    text = re.sub(r"[ \t]+", " ", text)

    # Normalize newlines
    text = re.sub(r"\n+", "\n", text)

    return text.strip()


def fix_broken_text(text):
    lines = text.split("\n")
    fixed_lines = []
    buffer = ""

    for line in lines:
        line = line.strip()

        if not line:
            continue

        # Merge very short fragments (OCR artifacts)
        if len(line) <= 3:
            buffer += " " + line
        else:
            if buffer:
                fixed_lines.append(buffer.strip())
                buffer = ""
            fixed_lines.append(line)

    if buffer:
        fixed_lines.append(buffer.strip())

    return "\n".join(fixed_lines)