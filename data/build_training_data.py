import re

import pandas as pd

from skills import KNOWN_SKILLS


def annotate_text(description):
    """
    Finds skills in a job description and returns them in spaCy training format.

    Parameters:
        description (str): Raw job description text

    Returns:
        tuple: (description, [(start, end, "SKILL"), ...])
    """
    matches = []
    for skill in KNOWN_SKILLS:
        skill_regex = r'\b' + re.escape(skill) + r'\b'
        for match in re.finditer(skill_regex, description, re.IGNORECASE):
            matches.append((match.start(), match.end(), "SKILL"))
    return (description, matches)

def build_training_data(df):
    """
    Loops through all job descriptions in the DataFrame, annotates each one,
    and returns a list of spaCy training examples.

    Parameters:
        df (DataFrame): Trimmed job postings DataFrame

    Returns:
        list: [(description, {"entities": [(start, end, "SKILL"), ...]}), ...]
    """