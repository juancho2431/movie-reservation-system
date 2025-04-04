from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.film_text import FilmText

router = APIRouter()

@router.get("/film-texts")
def get_film_texts(db: Session = Depends(get_db)):
    return db.query(FilmText).all()
