from fastapi import FastAPI, Depends # Used for Dependency Injection
from app.core.config import settings
from app.core.database import get_db
from sqlalchemy import text
from sqlalchemy.orm import Session

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {
        "status" : "healthy",
        "database" : "connected",
        "project" : settings.PROJECT_NAME,
        "version" : settings.VERSION,
        "environment" : settings.ENVIRONMENT
    }

