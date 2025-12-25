from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EmployerModel(Base):
    __tablename__ = "employers"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    industry = Column(String)
    location = Column(String)


class VacancyModel(Base):
    __tablename__ = "vacancies"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    salary = Column(Integer)
    employer_id = Column(Integer, ForeignKey("employers.id"))


class ResumeModel(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    experience = Column(Integer)
