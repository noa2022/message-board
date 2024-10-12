from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from models import Base, Message
from database import SessionLocal, engine

app = FastAPI()

class CreateRequest(BaseModel):
    name: str
    message: str
    password: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/messages/")
def create_message(request: CreateRequest, db: Session = Depends(get_db)):
    data = Message(name=request.name, message=request.message, password=request.password)

    db.add(data)
    db.commit()
    db.refresh(data)

    return data.id
