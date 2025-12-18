from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)

class ModuleData(Base):
    __tablename__ = "module_data"
    id = Column(Integer, primary_key=True, index=True)
    module = Column(String)
    name = Column(String)
