from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database import Base

class OrganizationUser(Base):
    __tablename__ = "organization_users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    organization_id = Column(Integer, ForeignKey("organizations.id"))
    role = Column(String(50), default="participant")

    user = relationship("User", back_populates="organizations")
    organization = relationship("Organization", back_populates="members")
