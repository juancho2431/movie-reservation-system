from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.payment import Payment

router = APIRouter()

@router.get("/payments")
def get_payments(db: Session = Depends(get_db)):
    return db.query(Payment).all()
