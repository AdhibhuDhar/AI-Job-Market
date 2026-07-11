from pydantic import BaseModel #pydantic so that we want our inputs to match expected schema,also for valdiation
from typing import Optional

class SkillSchema(BaseModel):
    languages: list[str]
    frameworks: list[str]
    databases: list[str]
    cloud : list[str]
    devops: list[str]
    ai_ml: list[str]
    tools : list[str]
    other : list[str]
class ProjectSchema(BaseModel):
    name:str
    technologies:list[str]
    description:str
    domain:str
class CandidateSchema(BaseModel):
    candidate_name: str
    experience_years: Optional[float]
    skills: SkillSchema
    projects: list[ProjectSchema]
    strengths: list[str]
    weaknesses: list[str]
    roles_suitable_for: list[str]
    industry_domains: list[str]
    certifications: Optional[list[str]]
    seniority_level: Optional[str]
    

