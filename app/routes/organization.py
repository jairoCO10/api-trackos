from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Organization, OrganizationUser
from app.schemas import OrganizationCreate, OrganizationRead
from app.utils.deps import get_db, get_current_user

router = APIRouter(prefix="/organizations")

@router.post("/", response_model=OrganizationRead)
def create_org(org: OrganizationCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    if db.query(Organization).filter(Organization.name == org.name).first():
        raise HTTPException(status_code=400, detail="Organization already exists")
    organization = Organization(name=org.name)
    db.add(organization)
    db.commit()
    db.refresh(organization)
    member = OrganizationUser(user_id=current_user.id, organization_id=organization.id, role="owner")
    db.add(member)
    db.commit()
    return organization

@router.get("/", response_model=list[OrganizationRead])
def list_orgs(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    memberships = db.query(OrganizationUser).filter_by(user_id=current_user.id).all()
    return [m.organization for m in memberships]
