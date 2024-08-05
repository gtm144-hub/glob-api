from fastapi import Depends, APIRouter
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text
import pandas as pd

from service.stats import get_query_results
from db_config import get_db
import repository.stats as qs

router = APIRouter()

@router.get("/employees-quarter")
def hired_employees_by_quarter(db:Session = Depends(get_db)):
    return get_query_results(db, qs.hiredEmployeesByQuarterQuery, qs.hiredEmployeesByQuarterHeader)

@router.get("/hired-count")
def hired_count(db:Session = Depends(get_db)):
    return get_query_results(db, qs.hiredCountOverAVGQuery, qs.hiredCountOverAVGHeader)

