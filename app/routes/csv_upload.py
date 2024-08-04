from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db_config import get_db
import service.csv_upload as cu

router = APIRouter()
@router.get("/department")
def upload_department_csv(db:Session =Depends(get_db)):
    return cu.get_dp(db=db)
