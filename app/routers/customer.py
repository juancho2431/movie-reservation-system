from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.customer import Customer

router = APIRouter()

@router.get("/customers")
def get_customers(db: Session = Depends(get_db)):
    customers = db.query(Customer).all()
    return [
        {
            "customer_id": c.customer_id,
            "name": f"{c.first_name} {c.last_name}",
            "email": c.email,
            "store_id": c.store_id
        }
        for c in customers
    ]
