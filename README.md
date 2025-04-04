# 🎬 Movie Reservation System

Sistema web completo para la **reserva de películas**, desarrollado con FastAPI en el backend y React en el frontend. Ideal para administrar el inventario de películas, gestionar clientes y facilitar reservas en tiendas físicas.

---

## 📁 Estructura del Proyecto

```
movie-reservation/
├── backend/              # FastAPI + SQLAlchemy
│   ├── app/
│   │   ├── models/
│   │   ├── routers/
│   │   ├── database.py
│   │   └── main.py
├── frontend/             # ReactJS 
│   ├── public/
│   └── src/
├── requirements.txt
└── README.md
```

---

## 🚀 Tecnologías Usadas

### 🛠️ Backend
- **FastAPI**
- **SQLAlchemy**
- **MySQL** (Sakila DB)
- **Uvicorn**
- **Pydantic**

### 💻 Frontend
- **ReactJS**
- **Axios**
- **Zustand** (estado global)
- **CSS Modules / Tailwind**

---

## ⚙️ Funcionalidades

- 🔍 Filtro por título y tienda para películas disponibles
- 📋 Consulta de usuarios con películas alquiladas
- 🧠 Precarga de datos usando Zustand
- ✅ Reserva de películas con cliente y película preseleccionada
- 🔄 Backend optimizado con subconsultas y joins eficientes
- 💬 Mensajes de confirmación y errores visuales
- 📆 Reserva automática con fecha actual

---

## 📦 Instalación

### 🐍 Backend (FastAPI)
```bash
cd backend
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 🌐 Frontend (React)
```bash
cd frontend
npm install
npm run dev
```

---

## 💾 Base de Datos

Este proyecto utiliza el esquema de **Sakila**, una base de datos ficticia para películas.  
Puedes usar **MySQL** para levantarla y conectarla con tu archivo `.env`.

---

## 📸 Capturas

> Puedes agregar aquí imágenes del dashboard, formulario de reserva, tablas de clientes, etc.

---

## ✨ Autor

**Juan Felipe**  
Desarrollador Full Stack  
Apasionado por el diseño, backend moderno y experiencias interactivas.  
📫 [GitHub](https://github.com/juancho2431)

---
