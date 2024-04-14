import React from "react";
import { Link, Outlet } from "react-router-dom";
import "./peliculas.css"; 

const Peliculas = () => {
    return (
        <div className="Peliculas">
            <h1>Peliculas</h1>
            <div className="peliculas-nav">
                <Link to="/peliculas/ver_peliculas">Ver peliculas</Link>
                <Link to="/peliculas/agregar_pelicula">Agregar pelicula</Link>
                <Link to="/peliculas/actualizar_pelicula">Actualizar pelicula</Link>
                <Link to="/peliculas/actualizar_pelicula">Borrar pelicula</Link>
                <Link to="/">Regresar</Link>
            </div>
            <Outlet />
        </div>
    );
};

export default Peliculas;