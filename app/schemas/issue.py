from pydantic import BaseModel
from typing import Optional

class IssueCreate(BaseModel):
    title: str
    description: Optional[str] = None
    project_id: int
    assignee_id: Optional[int] = None

class IssueRead(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: str
    project_id: int
    assignee_id: Optional[int]

    class Config:
        orm_mode = True
