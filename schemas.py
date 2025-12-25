from pydantic import BaseModel, Field
from typing import Optional, List

# Модель для работодателя
class Employer(BaseModel):
    id: int
    name: str
    industry: str
    location: str

# Модель для вакансии
class Vacancy(BaseModel):
    id: int
    title: str = Field(..., min_length=3, max_length=50, example="Python Developer")
    description: str
    salary: Optional[int] = Field(None, ge=0, le=1_000_000, example=2000)
    employer_id: int

# Модель для резюме
class Resume(BaseModel):
    id: int
    name: str
    skills: List[str] = Field(default=["Python", "FastAPI"])
    experience: Optional[int] = Field(0, ge=0, le=50, example=3)  # опыт в годах
