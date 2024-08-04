from fastapi import Depends, FastAPI, HTTPException

from db_config import Base, engine
from routes.csv_upload import router as crouter
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(crouter, prefix="/csv-upload")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
