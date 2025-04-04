from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.staff import Staff

router = APIRouter()

@router.get("/staff")
def get_staff(db: Session = Depends(get_db)):
    staff_list = db.query(Staff).all()
    
    # Eliminar 'picture' del resultado manualmente
    result = []
    for s in staff_list:
        staff_dict = s.__dict__.copy()
        staff_dict.pop("_sa_instance_state", None)
        staff_dict.pop("picture", None)
        result.append(staff_dict)
    
    return result

