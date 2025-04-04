from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.film_actor import FilmActor

router = APIRouter()

@router.get("/film-actors")
def get_film_actors(db: Session = Depends(get_db)):
    return db.query(FilmActor).all()
