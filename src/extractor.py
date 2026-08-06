import re

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