from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # 👈 Importar CORS
from app.database import engine, Base
from app.routers import (
    film, customer, rental, payment, staff, store, address,
    city, country, language, category, film_category, actor,
    film_actor, inventory, film_text, reservation, users_with_rentals
)

app = FastAPI()

# 🔐 Middleware CORS para permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # 👈 Origen del frontend React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔗 Rutas
app.include_router(film.router)
app.include_router(customer.router)
app.include_router(rental.router)
app.include_router(payment.router)
app.include_router(staff.router)
app.include_router(store.router)
app.include_router(address.router)
app.include_router(city.router)
app.include_router(country.router)
app.include_router(language.router)
app.include_router(category.router)
app.include_router(film_category.router)
app.include_router(actor.router)
app.include_router(film_actor.router)
app.include_router(inventory.router)
app.include_router(film_text.router)
app.include_router(reservation.router)
app.include_router(users_with_rentals.router)

# 🛠 Crear las tablas si no existen
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API de Reserva de Películas funcionando 🧾🎬"}
