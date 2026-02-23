from app.parser import extract_skills

def test_extract_skills():
    text = "Experienced Python and SQL developer"
    skills = extract_skills(text)
    assert "python" in skills