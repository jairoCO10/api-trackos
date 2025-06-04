from pydantic import BaseModel

class ProjectCreate(BaseModel):
    name: str
    organization_id: int

class ProjectRead(BaseModel):
    id: int
    name: str
    organization_id: int

    class Config:
        orm_mode = True
