from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.country import Country

router = APIRouter()

@router.get("/countries")
def get_countries(db: Session = Depends(get_db)):
    return db.query(Country).all()
