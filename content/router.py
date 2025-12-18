from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt

from app.database import SessionLocal
from app.models import ModuleData

router = APIRouter(prefix="/content", tags=["Content"])

security = HTTPBearer()
SECRET_KEY = "secret123"
ALGORITHM = "HS256"

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
    return True

@router.post("/")
def create_content(name: str, token=Depends(verify_token)):
    db: Session = SessionLocal()
    data = ModuleData(module="content", name=name)
    db.add(data)
    db.commit()
    return {"message": "Content created"}

@router.get("/")
def get_content(token=Depends(verify_token)):
    db: Session = SessionLocal()
    return db.query(ModuleData).filter(ModuleData.module == "content").all()
