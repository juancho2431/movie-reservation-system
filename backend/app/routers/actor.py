from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.actor import Actor

router = APIRouter()

@router.get("/actors")
def get_actors(db: Session = Depends(get_db)):
    return db.query(Actor).all()
