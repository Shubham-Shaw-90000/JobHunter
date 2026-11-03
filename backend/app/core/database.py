# Engine room for the DataBase layer

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from app.core.config import settings
from typing import Generator
from sqlalchemy.orm import Session

engine = create_engine(settings.DATABASE_URL, pool_pre_ping = True) #ppp checks connection and reconnects if dead

# autoflush : controls whether to flush the pending changes to DB before query
# bind : connects session factory to DB engine 
SessionLocal = sessionmaker(autocommit=False, autoflush= False, bind=engine) 

class Base(DeclarativeBase):
    pass

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db # temporarily hands the control and value to the caller function
                 # and pauses the current function to resume later
    finally:
        db.close()
                