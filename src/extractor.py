import spacy

# Generic list of skills that may appear on a job posting
KNOWN_SKILLS = [

]


def extract_skills(text):
    """
    Extracts technical skills from a job posting.

    Workflow:
        1. Keyword matching — checks if each skill in KNOWN_SKILLS appears in the text
        2. LLM fallback — passes text to an LLM to catch any skills missed by keyword matching (TODO)

    Parameters:
        text (str): Raw job posting text

    Returns:
        list of str: Skills found in the job posting e.g. ["Python", "Flask", "AWS"]
    """
    found = []

    for skill in KNOWN_SKILLS:
        if skill.lower() in text.lower():
            found.append(skill)

    return found