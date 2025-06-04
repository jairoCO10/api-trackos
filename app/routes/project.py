from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Project, ProjectUser, OrganizationUser
from app.schemas import ProjectCreate, ProjectRead
from app.utils.deps import get_db, get_current_user

router = APIRouter(prefix="/projects")

@router.post("/", response_model=ProjectRead)
def create_project(project: ProjectCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    # check if user is member of organization
    membership = db.query(OrganizationUser).filter_by(user_id=current_user.id, organization_id=project.organization_id).first()
    if not membership or membership.role not in ["owner", "admin"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    proj = Project(name=project.name, organization_id=project.organization_id)
    db.add(proj)
    db.commit()
    db.refresh(proj)
    member = ProjectUser(user_id=current_user.id, project_id=proj.id, role="owner")
    db.add(member)
    db.commit()
    return proj

@router.get("/organization/{org_id}", response_model=list[ProjectRead])
def list_projects(org_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    membership = db.query(OrganizationUser).filter_by(user_id=current_user.id, organization_id=org_id).first()
    if not membership:
        raise HTTPException(status_code=403, detail="Not member of organization")
    projects = db.query(Project).filter_by(organization_id=org_id).all()
    return projects
