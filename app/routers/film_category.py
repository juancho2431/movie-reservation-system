from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.film_category import FilmCategory

router = APIRouter()

@router.get("/film-categories")
def get_film_categories( db: Session = Depends(get_db)):
    return db.query(FilmCategory).all()
