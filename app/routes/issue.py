from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Issue, ProjectUser, Project
from app.schemas import IssueCreate, IssueRead
from app.utils.deps import get_db, get_current_user

router = APIRouter(prefix="/issues")

@router.post("/", response_model=IssueRead)
def create_issue(issue: IssueCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    membership = db.query(ProjectUser).filter_by(user_id=current_user.id, project_id=issue.project_id).first()
    if not membership:
        raise HTTPException(status_code=403, detail="Not a project member")
    db_issue = Issue(
        title=issue.title,
        description=issue.description,
        project_id=issue.project_id,
        assignee_id=issue.assignee_id
    )
    db.add(db_issue)
    db.commit()
    db.refresh(db_issue)
    return db_issue

@router.get("/project/{project_id}", response_model=list[IssueRead])
def list_issues(project_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    membership = db.query(ProjectUser).filter_by(user_id=current_user.id, project_id=project_id).first()
    if not membership:
        raise HTTPException(status_code=403, detail="Not a project member")
    issues = db.query(Issue).filter_by(project_id=project_id).all()
    return issues
