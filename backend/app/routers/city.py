from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.city import City

router = APIRouter()

@router.get("/cities")
def get_cities(db: Session = Depends(get_db)):
    return db.query(City).all()
