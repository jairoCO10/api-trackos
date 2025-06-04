from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database import Base

class ProjectUser(Base):
    __tablename__ = "project_users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))
    role = Column(String(50), default="participant")

    user = relationship("User", back_populates="projects")
    project = relationship("Project", back_populates="members")
