from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import select
from typing import List
from app.database import get_db
from app.models.rental import Rental
from app.models.customer import Customer
from app.models.inventory import Inventory
from app.models.film import Film

router = APIRouter()

@router.get("/current-rentals")
def get_users_with_active_rentals(db: Session = Depends(get_db)):
    # ✅ Obtener rentals sin return_date con joins a customer, inventory y film
    rentals = (
        db.query(Rental)
        .options(
            joinedload(Rental.customer),
            joinedload(Rental.inventory).joinedload(Inventory.film)
        )
        .filter(Rental.return_date == None)
        .all()
    )

    # Agrupar por usuario
    users_dict = {}

    for rental in rentals:
        customer = rental.customer
        film = rental.inventory.film
        user_id = customer.customer_id

        if user_id not in users_dict:
            users_dict[user_id] = {
                "customer_id": user_id,
                "name": f"{customer.first_name} {customer.last_name}",
                "email": customer.email,
                "rentals": []
            }

        users_dict[user_id]["rentals"].append({
            "film_id": film.film_id,
            "title": film.title,
            "rental_date": rental.rental_date,
            "store_id": rental.inventory.store_id
        })

    return list(users_dict.values())
