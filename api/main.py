from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from models import Base, Message
from database import SessionLocal, engine

app = FastAPI()

class CreateRequest(BaseModel):
    name: str
    message: str
    password: str


class UpdateRequest(BaseModel):
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


@app.get("/messages/")
def read_root(db: Session = Depends(get_db)):
    data = db.query(Message).all()
    if not data:
        raise HTTPException(status_code=404, detail="Message not found")
    return data


@app.post("/messages/")
def create_message(request: CreateRequest, db: Session = Depends(get_db)):
    data = Message(name=request.name, message=request.message, password=request.password)

    db.add(data)
    db.commit()
    db.refresh(data)

    return data.id


@app.delete("/messages/{message_id}")
def delete_message(message_id: int, db: Session = Depends(get_db)):
    data = db.query(Message).filter(Message.id == message_id).first()
    
    if not data:
        raise HTTPException(status_code=404, detail="Message not found")
        
    data.deleted_at = datetime.now()
    db.commit()

    return {"detail": "Message deleted successfully"}


@app.put("/messages/{message_id}")
def update_message(request: UpdateRequest, message_id: int, db: Session = Depends(get_db)):
    data = db.query(Message).filter(Message.id == message_id).first()

    if not data:
        raise HTTPException(status_code=404, detail="Message not found")

    data.name = request.name
    data.message = request.message
    data.password = request.password

    db.commit()
    db.refresh(data)

    return data.id

    