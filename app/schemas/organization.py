from pydantic import BaseModel

class OrganizationCreate(BaseModel):
    name: str

class OrganizationRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
