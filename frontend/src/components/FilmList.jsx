import React, { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import "./FilmList.css";

function FilmList() {
  const [films, setFilms] = useState([]);
  const [filtered, setFiltered] = useState([]);
  const [search, setSearch] = useState("");
  const [storeFilter, setStoreFilter] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/available-films")
      .then((res) => {
        const results = Array.isArray(res.data) ? res.data : res.data.results || [];
        const grouped = {};
        results.forEach((item) => {
          const key = `${item.title}_${item.store_id}`;
          if (!grouped[key]) {
            grouped[key] = {
              title: item.title,
              store_id: item.store_id,
              stock: 0,
              inventory_id: item.inventory_id,
              film_id: item.film_id, // Para pasarlo al formulario
            };
          }
          grouped[key].stock += 1;
        });
        setFilms(Object.values(grouped));
      })
      .catch((err) => {
        console.error("Error al obtener las películas:", err);
        setFilms([]);
      });
  }, []);

  useEffect(() => {
    let data = [...films];
    if (storeFilter) {
      data = data.filter((f) => f.store_id === Number(storeFilter));
    }
    if (search) {
      data = data.filter((f) => f.title.toLowerCase().includes(search.toLowerCase()));
    }
    setFiltered(data);
  }, [films, search, storeFilter]);

  const handleReserve = (film) => {
    navigate("/reserve", {
      state: {
        film_id: film.film_id,
        title: film.title,
        store_id: film.store_id,
      },
    });
  };

  return (
    <div className="film-container">
      <h2 className="film-title">🎬 Películas Disponibles</h2>

      <div className="film-filters">
        <input
          type="text"
          className="film-input"
          placeholder="🔍 Buscar por título..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
        <select
          className="film-select"
          value={storeFilter}
          onChange={(e) => setStoreFilter(e.target.value)}
        >
          <option value="">🏪 Todas las tiendas</option>
          <option value="1">Tienda 1</option>
          <option value="2">Tienda 2</option>
        </select>
      </div>

      <div className="film-table-wrapper">
        <table className="film-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Tienda</th>
              <th>Película</th>
              <th>Stock</th>
              <th>Acción</th>
            </tr>
          </thead>
          <tbody>
            {filtered.length > 0 ? (
              filtered.map((film) => (
                
// Reemplaza este fragmento dentro del .map de la tabla:
<tr key={`${film.title}-${film.store_id}`}>
  <td>{film.inventory_id}</td>
  <td>{film.store_id}</td>
  <td>{film.title}</td>
  <td>{film.stock}</td>
  <td>
    <button
      className="btn-reservar"
      onClick={() => navigate(`/reservar?inventory_id=${film.inventory_id}&title=${encodeURIComponent(film.title)}&store_id=${film.store_id}`)}
    >
      Reservar
    </button>
  </td>
</tr>
              ))
            ) : (
              <tr>
                <td colSpan="5" className="no-results">
                  ❌ No se encontraron películas
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default FilmList;
