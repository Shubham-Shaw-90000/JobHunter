
# === Defines how the data is Retreived , Validated, and Returned through the API

from pydantic import BaseModel, ConfigDict, EmailStr

class CandidateProfileBase(BaseModel):
    full_name: str
    email: EmailStr
    phone: str | None=None
    college: str
    degree: str
    branch: str
    graduation_year: int
    cgpa: float

class CandidateProfileCreate(CandidateProfileBase):
    # Schema used when creating a new profile via POST request
    pass

class CandidateProfileUpdate(BaseModel):
    # Schema used when updating profile using PATCH request
    # Every Field is Optional

    full_name: str | None=None
    email: Emailstr | None=None
    phone: str | None=None
    college: str | None=None
    degree: str | None=None
    branch: str | None=None
    graduation_year: int | None=None
    cgpa: float | None=None

class CandidateProfileResponse(CandidateProfileBase):
    # Schema used to return back to the client in response
    
    id: int
    model_config = ConfigDict(from_attributes=True) #Helps in defining the rules for the Schema


# === SKILLS SCHEMA ===

class SkillBase(BaseModel):
    name:str
    category: str

class SkillCreate(SkillBase):
    pass

class SkillResponse(SkillBase):
    id: int

    model_config = ConfigDict(from_attributes=True)