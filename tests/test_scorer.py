from app.scorer import calculate_score

def test_score_range():
    score = calculate_score(["python", "sql"], ["python", "sql", "django"])
    assert 0 <= score <= 100