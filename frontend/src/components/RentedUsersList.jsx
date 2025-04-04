import React, { useEffect, useState } from "react";
import axios from "axios";
import "./RentedUsersList.css";

function RentedUsers() {
  const [users, setUsers] = useState([]);
  const [filteredUsers, setFilteredUsers] = useState([]);
  const [search, setSearch] = useState("");
  const [orderByDate, setOrderByDate] = useState(true);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get("http://localhost:8000/current-rentals")
      .then((res) => {
        const data = Array.isArray(res.data) ? res.data : [];

        // Ordenar alquileres dentro de cada usuario
        data.forEach(user => {
          user.rentals.sort((a, b) => new Date(b.rental_date) - new Date(a.rental_date));
          user.latestRentalDate = user.rentals.length > 0 ? new Date(user.rentals[0].rental_date) : null;
        });

        // Ordenar usuarios por fecha más reciente
        data.sort((a, b) => b.latestRentalDate - a.latestRentalDate);

        setUsers(data);
        setFilteredUsers(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Error al obtener usuarios:", err);
        setError("❌ No se pudo cargar la información");
        setLoading(false);
      });
  }, []);

  useEffect(() => {
    let data = [...users];

    if (search.trim()) {
      const searchLower = search.toLowerCase();
      data = data.filter(user => user.name?.toLowerCase().includes(searchLower));
    }

    if (orderByDate) {
      data.sort((a, b) => b.latestRentalDate - a.latestRentalDate);
    }

    setFilteredUsers(data);
  }, [search, orderByDate, users]);

  if (loading) {
    return (
      <div className="rented-container">
        <p className="loading">⏳ Cargando usuarios con películas alquiladas...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="rented-container">
        <p className="error">{error}</p>
      </div>
    );
  }

  return (
    <div className="rented-container">
      <h2 className="rented-title">🎟️ Usuarios con Películas Alquiladas</h2>

      <div className="filters">
        <input
          className="rented-search"
          type="text"
          placeholder="🔍 Buscar por nombre..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
        
      </div>

      {filteredUsers.length === 0 ? (
        <p className="empty">🔍 No hay usuarios con alquileres activos.</p>
      ) : (
        <div className="rented-grid">
          {filteredUsers.map((user) => (
            <div className="user-card" key={user.customer_id}>
              <div className="user-header">
                <h3>👤 {user.name}</h3>
                <p className="user-id">ID: {user.customer_id}</p>
              </div>
              <p className="email">📧 {user.email}</p>
              <ul className="rental-list">
                {user.rentals.map((rental, idx) => (
                  <li key={idx}>
                    🎬 <strong>{rental.title}</strong> — 🏪 Tienda {rental.store_id}<br />
                    <span className="date">📅 {new Date(rental.rental_date).toLocaleDateString()}</span>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default RentedUsers;
