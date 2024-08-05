from fastapi import Depends, APIRouter, UploadFile, File
from sqlalchemy.orm import Session

from db_config import get_db, Department, Job, Employee
from service.csv_upload import upload_to_db
from utils.models import department_types, job_types, employee_types

router = APIRouter()

@router.post("/department")
async def upload_department_csv(file: UploadFile = File(...), db:Session = Depends(get_db)):
    return await upload_to_db(file, db, department_types, Department)

@router.post("/job")
async def upload_job_csv(file: UploadFile = File(...), db:Session = Depends(get_db)):
    return await upload_to_db(file, db, job_types, Job)

@router.post("/employee")
async def upload_employee_csv(file: UploadFile = File(...), db:Session = Depends(get_db)):
    return await upload_to_db(file, db, employee_types, Employee)
