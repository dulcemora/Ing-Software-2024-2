import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link
} from "react-router-dom";
import Home from "./components/home";
import Clientes from "./components/clientes";
import Peliculas from "./components/peliculas";
import Rentas from "./components/rentas";
import Ver_clientes from "./components/clientes/ver_clientes";
import Actualizar_cliente from "./components/clientes/actualizar_cliente";
import Agregar_cliente from "./components/clientes/agregar_cliente";
import Borrar_cliente from "./components/clientes/borrar_cliente";
import Ver_peliculas from "./components/peliculas/ver_peliculas";
import Actualizar_pelicula from "./components/peliculas/actualizar_pelicula";
import Agregar_pelicula from "./components/peliculas/agregar_pelicula";
import Borrar_pelicula from "./components/peliculas/borrar_pelicula";
import Ver_rentas from "./components/renta/ver_rentas";
import Actualizar_renta from "./components/renta/actualizar_renta";
import Agregar_renta from "./components/renta/agregar_renta";
import "./App.css";

function App() {
  return (
    <Router>
      <div className="App">
        <ul className="App-header">
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/clientes">Clientes</Link>
          </li>
          <li>
            <Link to="/peliculas">Peliculas</Link>
          </li>
          <li>
            <Link to="/rentas">Rentas</Link>
          </li>
        </ul>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/clientes" element={<Clientes />} />
            <Route path="ver_clientes" element={<Ver_clientes />} />
            <Route path="actualizar_cliente" element={<Actualizar_cliente />} />
            <Route path="agregar_cliente" element={<Agregar_cliente />} />
            <Route path="borrar_cliente" element={<Borrar_cliente />} />
          <Route path="/peliculas" element={<Peliculas />} />
            <Route path="ver_peliculas" element={<Ver_peliculas />} />
            <Route path="actualizar_pelicula" element={<Actualizar_pelicula />} />
            <Route path="agregar_pelicula" element={<Agregar_pelicula />} />
            <Route path="borrar_pelicula" element={<Borrar_pelicula />} />
          <Route path="/rentas" element={<Rentas />}>
            <Route path="ver_rentas" element={<Ver_rentas />} />
            <Route path="actualizar_renta" element={<Actualizar_renta />} />
            <Route path="agregar_renta" element={<Agregar_renta />} />
          </Route>
        </Routes>
      </div>
    </Router>
  );
}

export default App;