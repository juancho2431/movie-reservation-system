from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.inventory import Inventory

router = APIRouter()

@router.get("/inventories")
def get_inventories(db: Session = Depends(get_db)):
    return db.query(Inventory).all()
