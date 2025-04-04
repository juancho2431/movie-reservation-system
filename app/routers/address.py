from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.address import Address

router = APIRouter()

@router.get("/addresses")
def get_addresses(db: Session = Depends(get_db)):
    addresses = db.query(Address).all()

    # Opcional: excluir campo 'location' si da problemas de serialización
    result = []
    for addr in addresses:
        addr_dict = addr.__dict__.copy()
        addr_dict.pop("_sa_instance_state", None)
        addr_dict.pop("location", None)
        result.append(addr_dict)

    return result
