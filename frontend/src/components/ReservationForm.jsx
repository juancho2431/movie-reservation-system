import React, { useEffect, useState } from "react";
import axios from "axios";
import "./ReservationForm.css";
import { useLocation } from "react-router-dom";

function ReservationForm() {
  const [films, setFilms] = useState([]);
  const [customers, setCustomers] = useState([]);
  const [selectedFilm, setSelectedFilm] = useState(null);
  const [selectedCustomer, setSelectedCustomer] = useState(null);
  const [searchCustomer, setSearchCustomer] = useState("");
  const [success, setSuccess] = useState(null);

  const location = useLocation();
  const params = new URLSearchParams(location.search);
  const initialInventoryId = params.get("inventory_id");

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [filmRes, customerRes] = await Promise.all([
          axios.get("http://localhost:8000/available-films"),
          axios.get("http://127.0.0.1:8000/customers")
        ]);

        const filmResults = Array.isArray(filmRes.data.results) ? filmRes.data.results : [];
        setFilms(filmResults);

        // Si hay una película pasada por la URL, la precargamos
        if (initialInventoryId) {
          const preselected = filmResults.find(f => f.inventory_id === Number(initialInventoryId));
          if (preselected) setSelectedFilm(preselected);
        }

        const customerResults = Array.isArray(customerRes.data) ? customerRes.data : [];
        setCustomers(customerResults);
      } catch (error) {
        console.error("Error cargando datos:", error);
      }
    };

    fetchData();
  }, [initialInventoryId]);

  const handleReservation = async () => {
    if (!selectedFilm || !selectedCustomer) {
      setSuccess("❌ Selecciona una película y un cliente.");
      return;
    }

    try {
      await axios.post("http://localhost:8000/reserve", {
        inventory_id: selectedFilm.inventory_id,
        customer_id: selectedCustomer.customer_id,
      });
      setSuccess("✅ Reserva realizada exitosamente.");
    } catch (err) {
      console.error(err);
      setSuccess("❌ Error al hacer la reserva.");
    }
  };

  const filteredCustomers = customers.filter((c) =>
    c.name?.toLowerCase().includes(searchCustomer.toLowerCase())
  );

  return (
    <div className="reservation-container">
      <h2 className="form-title">🎟️ Formulario de Reserva</h2>

      <div className="form-section">
        <label>🎬 Película</label>
        <select
          value={selectedFilm?.inventory_id || ""}
          onChange={(e) => {
            const selected = films.find(f => f.inventory_id === Number(e.target.value));
            setSelectedFilm(selected);
          }}
        >
          <option value="">-- Selecciona una película --</option>
          {films.map(film => (
            <option key={film.inventory_id} value={film.inventory_id}>
              {film.title} (Tienda {film.store_id})
            </option>
          ))}
        </select>
      </div>

      <div className="form-section">
        <label>👤 Cliente</label>
        
        <select
          value={selectedCustomer?.customer_id || ""}
          onChange={(e) => {
            const selected = customers.find(c => c.customer_id === Number(e.target.value));
            setSelectedCustomer(selected);
          }}
        >
          <option value="">-- Selecciona un cliente --</option>
          {filteredCustomers.map(customer => (
            <option key={customer.customer_id} value={customer.customer_id}>
              {customer.name}
            </option>
          ))}
        </select>
      </div>

      <button onClick={handleReservation}>📦 Reservar Película</button>
      {success && <p className="reservation-message">{success}</p>}
    </div>
  );
}

export default ReservationForm;
