from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.film import Film

router = APIRouter()

@router.get("/films")
def get_films(db: Session = Depends(get_db)):
    return db.query(Film).all()
