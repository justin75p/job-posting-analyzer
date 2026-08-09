from skills import KNOWN_SKILLS

def annotate_text(description):
    """
    Finds skills in a job description and returns them in spaCy training format.

    Parameters:
        description (str): Raw job description text

    Returns:
        tuple: (description, [(start, end, "SKILL"), ...])
    """

def build_training_data(df):
    """
    Loops through all job descriptions in the DataFrame, annotates each one,
    and returns a list of spaCy training examples.

    Parameters:
        df (DataFrame): Trimmed job postings DataFrame

    Returns:
        list: [(description, {"entities": [(start, end, "SKILL"), ...]}), ...]
    """