def extract_skills(text):
    skills_db = ["python", "sql", "django", "java"]
    text = text.lower()
    found = []

    for skill in skills_db:
        if skill in text:
            found.append(skill)

    return found