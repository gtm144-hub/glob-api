import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DateTime, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Department(Base):
    __tablename__ = "departments"

    #TODO Look for database index optimizations improvements
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Job(Base):
    __tablename__ = "jobs"

    #TODO Look for database index optimizations improvements
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    datetime = Column(DateTime)
    department_id = Column(Integer, ForeignKey("departments.id"))
    job_id = Column(Integer, ForeignKey("jobs.id"))
