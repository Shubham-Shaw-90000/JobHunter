
# === Defines the Actual Business Logic , it acts as the layer 
# between the API endpoints and the Database Operations

from sqlalchemy.orm import Session
from app.modules.candidate.models import CandidateProfile
from app.modules.candidate.schemas import CandidateProfileCreate , CandidateProfileUpdate

def get_candidate(db: Session) -> CandidateProfile | None:
    return db.query(CandidateProfile).first()

def create_candidate(db: Session, profile_in: CandidateProfileCreate) -> CandidateProfile:
    data_dict = profile_in.model_dump()
    db_profile = CandidateProfile(**data_dict) # ** operator (dictionary unpacking) takes a dictionary and unpacks it as keyword arguments into a class constructor
    db.add(db_profile) # add object to the session transaction
    db.commit() # commit changes to PostGres completely
    db.refresh(db_profile) # refresh to re-read the stores data
    return db_profile

def update_candidate(db:Session, candidate_id:int, profile_in: CandidateProfileUpdate ) -> CandidateProfile | None:
    db_candidate = db.query(CandidateProfile).filter(CandidateProfile.id == candidate_id).first()
    if db_candidate is None:
        return None
    data = profile_in.model_dump(exclude_unset=True) #excludes fields the user did not explicitly provide
    for key, value in data.items():
        setattr(db_candidate,key,value)
    db.commit()
    db.refresh(db_candidate)
    return db_candidate


