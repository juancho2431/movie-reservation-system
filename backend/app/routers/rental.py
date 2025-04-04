from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.rental import Rental

router = APIRouter()

@router.get("/rentals")
def get_rentals(db: Session = Depends(get_db)):
    return db.query(Rental).all()
