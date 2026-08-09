import re

import spacy

from skills import KNOWN_SKILLS


def extract_skills(text):
    """
    Extracts technical skills from text from either job postings or resumes.

    Workflow:
        1. Custom spaCy NER model — identifies skills in text (TODO)
        2. KNOWN_SKILLS keyword matching — catches anything NER missed
        3. spaCy dependency parsing — classifies each skill as required or preferred (TODO)
        4. LLM fallback — catches edge cases (TODO)

    Parameters:
        text (str): Raw text from either a job posting or a resume.

    Returns:
        dict: {
            "required": ["Python", "AWS"],
            "preferred": ["Docker", "React"]
        }
    Note: when used on a resume, all skills returned under "required"
    """