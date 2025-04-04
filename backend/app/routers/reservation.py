from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import select
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from app.database import get_db
from app.models.inventory import Inventory
from app.models.film import Film
from app.models.rental import Rental

router = APIRouter()

# 🔹 MODELO PARA RESERVA
class ReservationRequest(BaseModel):
    inventory_id: int
    customer_id: int

# 🔹 ENDPOINT DISPONIBILIDAD DE PELÍCULAS
@router.get("/available-films")
def get_available_films(
    store_id: Optional[int] = None,
    title: Optional[str] = None,
    db: Session = Depends(get_db)
):
    # Subconsulta para inventarios rentados
    rented_subquery = select(Rental.inventory_id).where(Rental.return_date == None).subquery()

    # Query principal
    query = (
        db.query(Inventory)
        .join(Film, Inventory.film_id == Film.film_id)
        .options(joinedload(Inventory.film))
        .filter(~Inventory.inventory_id.in_(rented_subquery))
    )

    if store_id:
        query = query.filter(Inventory.store_id == store_id)

    if title:
        query = query.filter(Film.title.ilike(f"%{title}%"))

    query = query.order_by(Film.title).limit(500)
    items = query.all()

    results = [
        {
            "inventory_id": item.inventory_id,
            "film_id": item.film.film_id,
            "title": item.film.title,
            "store_id": item.store_id
        }
        for item in items
    ]

    return {
        "total": len(results),
        "results": results,
        "note": "🔹 Mostrando hasta 500 resultados. Usa filtros para mejores resultados."
    }

# 🔹 ENDPOINT PARA RESERVAR PELÍCULA
@router.post("/reserve")
def reserve_film(data: ReservationRequest, db: Session = Depends(get_db)):
    new_rental = Rental(
        inventory_id=data.inventory_id,
        customer_id=data.customer_id,
        rental_date=datetime.utcnow(),
        staff_id=1,  # Puedes hacerlo dinámico si deseas
        last_update=datetime.utcnow()
    )
    db.add(new_rental)
    db.commit()
    return {"message": "✅ Reserva realizada con éxito"}
