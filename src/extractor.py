import spacy

KNOWN_SKILLS = [
    # Programming Languages
    "Python", "Java", "JavaScript", "TypeScript", "C++", "C#", "R", "Go", "Rust", "Swift", "Kotlin", "SQL",

    # Web Frameworks
    "Flask", "Django", "FastAPI", "React", "Vue", "Angular", "Express", "Spring", "Next.js", "Node.js",

    # Databases
    "PostgreSQL", "MySQL", "MongoDB", "SQLite", "Redis", "Elasticsearch", "DynamoDB", "Cassandra",

    # Cloud
    "AWS", "Azure", "GCP", "Lambda", "S3", "EC2", "RDS", "CloudFormation", "Terraform", "Docker", "Kubernetes",

    # ML / Data Science
    "scikit-learn", "TensorFlow", "PyTorch", "Keras", "pandas", "NumPy", "spaCy", "NLTK", "Hugging Face", "XGBoost",

    # Tools
    "Git", "GitHub", "Linux", "REST APIs", "GraphQL", "CI/CD", "Jenkins", "Jira", "Postman",

    # Data / Analytics
    "Tableau", "Power BI", "Spark", "Hadoop", "Airflow", "dbt", "Snowflake", "BigQuery",

    # APIs / Protocols
    "JSON", "XML", "gRPC", "WebSocket", "OAuth",

    # Mobile
    "React Native", "Flutter", "Android", "iOS",

    # Testing
    "pytest", "JUnit", "Selenium", "Jest",

    # Concepts
    "machine learning", "deep learning", "NLP", "computer vision", "data analysis", "agile", "object-oriented programming",

    # Other
    "Streamlit", "Jupyter", "MATLAB", "Bash", "PowerShell", "Excel"
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