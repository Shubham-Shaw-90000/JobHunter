
#  === Defines how the data is stored in the Database

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from app.core.database import Base
from pydantic import EmailStr

class CandidateProfile(Base):
    __tablename__ = "candidate_profiles"

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    full_name: Mapped[str] = mapped_column(String(100),index=True)
    email: Mapped[EmailStr] = mapped_column(String(100),unique=True,index=True)
    phone: Mapped[str | None] = mapped_column(String(20),nullable=True)
    college: Mapped[str] = mapped_column(String(200))
    degree: Mapped[str] = mapped_column(String(200))
    branch: Mapped[str] = mapped_column(String(100))
    graduation_year: Mapped[int] = mapped_column()
    cgpa: Mapped[float] = mapped_column()

    # Relationships to Candidate Skills
    skills: Mapped[list["CandidateSkill"]] = relationship(back_populates="candidate",cascade="all, delete-orphan")

class Skills(Base):
    __tablename__="skills"

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name: Mapped[str] = mapped_column(String(50),unique=True, index=True)
    category: Mapped[str] = mapped_column(String(50))

class CandidateSkill(Base):
    __tablename__ = "candidate_skills"

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    candidate_id: Mapped[int] = mapped_column(ForeignKey("candidate_profiles.id",ondelete="CASCADE"))
    skill_id: Mapped[int] = mapped_column(ForeignKey("skills.id",ondelete="CASCADE"))
    proficiency: Mapped[str] = mapped_column(String(20),default="beginner")
    status: Mapped[str] = mapped_column(String(20),default="learning")
    evidence: Mapped[str | None] = mapped_column(String(250),nullable=True)

    # Relationships
    candidate: Mapped["CandidateProfile"] = relationship(back_populates="skills") #back_populates establishes the 2 sides of an ORM relationship
    skill: Mapped["Skills"] = relationship() #python level relationship
