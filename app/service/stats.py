from fastapi import HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from sqlalchemy import text
import pandas as pd


def get_query_results(db: Session, query: str, columns: list):
    try:
        result = db.execute(text(query))
        df = pd.DataFrame(result, columns=columns)

        return HTMLResponse(content = df.to_html(), status_code = 200)
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
