import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import FilmList from "./components/FilmList";
import RentedUsers from "./components/RentedUsersList";
import ReservationForm from "./components/ReservationForm";

function App() {
  return (
    <Router>
      <div style={{
        minHeight: "100vh",
        background: "linear-gradient(135deg, #f0f4ff, #ffffff)",
        fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
        color: "#1a1a1a",
        padding: "2rem"
      }}>
        <header style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          marginBottom: "2rem"
        }}>
          <h1 style={{
            fontSize: "2rem",
            fontWeight: "bold",
            color: "#4f46e5",
            margin: 0
          }}>
            🎥 Movie Rental System
          </h1>

          <nav style={{ display: "flex", gap: "1rem" }}>
            <Link to="/films" style={navBtnStyle}>🎬 Ver Películas</Link>
            <Link to="/rented-users" style={navBtnStyle}>👥 Usuarios con Alquiler</Link>
          </nav>
        </header>

        <main style={{ padding: "1rem", background: "#fff", borderRadius: "12px", boxShadow: "0 0 15px rgba(0,0,0,0.05)" }}>
          <Routes>
            <Route path="/films" element={<FilmList />} />
            <Route path="/reservar" element={<ReservationForm />} />
            <Route path="/rented-users" element={<RentedUsers />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

// 💅 Estilo para botones de navegación
const navBtnStyle = {
  background: "#4f46e5",
  padding: "0.6rem 1.2rem",
  borderRadius: "8px",
  color: "white",
  textDecoration: "none",
  fontWeight: "500",
  transition: "all 0.2s ease-in-out",
  boxShadow: "0 4px 6px rgba(0,0,0,0.1)"
};

export default App;
