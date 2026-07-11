#well use optional becz not eg 0-1 yrs exp or 2+ exp,cant be mentioned by a single digit explicitly
#so pydantic will validate the input data and ensure its similarity to the expected schema,also for validation
from pydantic import BaseModel #basemodel is the base class for creating pydantic models,provides data validation and parsing
from typing import Optional
class JobSchema(BaseModel):
    title:str
    mandatory_skills:list[str]=[] #mpt list as default
    required_skills:list[str]
    preferred_skills:list[str]=[]
    experience_required:Optional[float]=None #so that if not provided,will be None
