from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.store import Store

router = APIRouter()

@router.get("/stores")
def get_stores(db: Session = Depends(get_db)):
    return db.query(Store).all()
