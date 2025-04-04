from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.language import Language

router = APIRouter()

@router.get("/languages")
def get_languages(db: Session = Depends(get_db)):
    return db.query(Language).all()
