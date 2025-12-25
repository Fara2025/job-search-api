from fastapi import FastAPI, Query, Path, Body
from typing import List, Optional
from schemas import Vacancy, Employer, Resume
from data import vacancies, employers, resumes

app = FastAPI(title="Job Search API", version="1.0")

# --- Query параметры ---
@app.get("/vacancies")
def get_vacancies(
    min_salary: Optional[int] = Query(0, ge=0, example=1000),
    max_salary: Optional[int] = Query(1_000_000, le=1_000_000, example=5000),
    keyword: Optional[str] = Query(None, min_length=2, max_length=20, example="Python")
):
    results = [
        v for v in vacancies 
        if v.salary >= min_salary and v.salary <= max_salary
        and (keyword.lower() in v.title.lower() if keyword else True)
    ]
    return {"vacancies": results}

# --- Path параметры ---
@app.get("/vacancies/{vacancy_id}")
def get_vacancy_by_id(
    vacancy_id: int = Path(..., ge=1, example=1)
):
    for v in vacancies:
        if v.id == vacancy_id:
            return v
    return {"error": "Vacancy not found"}

# --- Body (создание вакансии) ---
@app.post("/vacancies", response_model=Vacancy)
def create_vacancy(vacancy: Vacancy = Body(..., example={
    "id": 3,
    "title": "DevOps Engineer",
    "description": "CI/CD, Kubernetes",
    "salary": 4000,
    "employer_id": 1
})):
    vacancies.append(vacancy)
    return vacancy

# --- Nested models (работодатель + вакансии) ---
@app.get("/employers/{employer_id}")
def get_employer_with_vacancies(employer_id: int):
    for e in employers:
        if e.id == employer_id:
            related_vacancies = [v for v in vacancies if v.employer_id == e.id]
            return {"employer": e, "vacancies": related_vacancies}
    return {"error": "Employer not found"}

# --- Работа с резюме ---
@app.get("/resumes")
def list_resumes(skill: Optional[str] = Query(None, example="Python")):
    if skill:
        return [r for r in resumes if skill in r.skills]
    return resumes
@app.put("/vacancies/{vacancy_id}", response_model=Vacancy)
def update_vacancy(vacancy_id: int, updated: Vacancy):
    for index, v in enumerate(vacancies):
        if v.id == vacancy_id:
            vacancies[index] = updated
            return updated
    return {"error": "Vacancy not found"}
@app.delete("/vacancies/{vacancy_id}")
def delete_vacancy(vacancy_id: int):
    for v in vacancies:
        if v.id == vacancy_id:
            vacancies.remove(v)
            return {"message": "Vacancy deleted successfully"}
    return {"error": "Vacancy not found"}
@app.post("/resumes", response_model=Resume)
def create_resume(resume: Resume):
    resumes.append(resume)
    return resume
