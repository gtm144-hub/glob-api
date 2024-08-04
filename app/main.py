from typing import Union
from fastapi import Depends, FastAPI, HTTPException
from db_config import SessionLocal, Base, engine, Job, Department, Employee
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_job(db: Session):
    return db.query(Job).first()

@app.get("/")
def read_root(db:Session =Depends(get_db)):
    return get_job(db=db)


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
