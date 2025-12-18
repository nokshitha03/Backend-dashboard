from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt

from app.database import SessionLocal
from app.models import ModuleData

router = APIRouter(prefix="/analytics", tags=["Analytics"])

security = HTTPBearer()
SECRET_KEY = "secret123"
ALGORITHM = "HS256"

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
    return True

@router.post("/")
def create_analytics(name: str, token=Depends(verify_token)):
    db: Session = SessionLocal()
    data = ModuleData(module="analytics", name=name)
    db.add(data)
    db.commit()
    return {"message": "Analytics data created"}

@router.get("/")
def get_analytics(token=Depends(verify_token)):
    db: Session = SessionLocal()
    return db.query(ModuleData).filter(ModuleData.module == "analytics").all()
