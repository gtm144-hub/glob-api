from sqlalchemy.orm import Session
from sqlalchemy import insert

def insert_data(db: Session, data: dict, model):
    with db.begin():
        db.execute(insert(model).values(data))
        db.commit()
    return

