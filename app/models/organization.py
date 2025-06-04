from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True)

    members = relationship("OrganizationUser", back_populates="organization")
    projects = relationship("Project", back_populates="organization")
