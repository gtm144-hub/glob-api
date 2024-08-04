from db_config import Job, Department, Employee
from sqlalchemy.orm import Session

def get_dp(db: Session):
    return db.query(Department).first()

