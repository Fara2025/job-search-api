from schemas import Vacancy, Employer, Resume


employers = [
    Employer(id=1, name="Google", industry="IT", location="USA"),
    Employer(id=2, name="Yandex", industry="IT", location="Russia"),
]

vacancies = [
    Vacancy(id=1, title="Backend Developer", description="FastAPI, Docker", salary=3000, employer_id=1),
    Vacancy(id=2, title="Data Analyst", description="SQL, Python", salary=2000, employer_id=2),
]

resumes = [
    Resume(id=1, name="Fara", skills=["Python", "FastAPI", "SQL"], experience=2),
    Resume(id=2, name="Ali", skills=["JavaScript", "React"], experience=1),
]
