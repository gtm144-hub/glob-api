import repository.csv_upload as cu
from sqlalchemy.orm import Session

def get_dp(db: Session):
    return cu.get_dp(db)
