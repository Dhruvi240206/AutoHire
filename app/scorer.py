def calculate_score(found_skills, required_skills):
    match_count = len(set(found_skills) & set(required_skills))
    score = (match_count / len(required_skills)) * 100
    return score