from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi import UploadFile, HTTPException
import pandas as pd
import io 

from repository.csv_upload import insert_data

CHUNCK_FILE_SIZE = 1024 * 1024

async def upload_to_db(file: UploadFile, db: Session, type_list: dict, model):

    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a CSV file.")
    
    try:
        print("DESASDF")
        while chunk := await file.read(CHUNCK_FILE_SIZE):
            decoded_content = chunk.decode('utf-8')
            pd_chunck = pd.read_csv(io.StringIO(decoded_content))
            df = pd_chunck.astype(type_list)
            data = df.to_dict(orient='records')

            insert_data(db, data, model)

        return JSONResponse(
            content={
                "message": f"Successfully processed {file.filename}"
            },
            status_code=200
        )
    
    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="Invalid file encoding. Please ensure the CSV file is UTF-8 encoded.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
