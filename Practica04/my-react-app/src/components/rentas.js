import React from "react";
import { Link, Outlet } from "react-router-dom";
import "./rentas.css"; 

const Rentas = () => {
    return (
        <div className="Rentas">
            <h1>Rentas</h1>
            <div className="rentas-nav">
                <Link to="/rentas/ver_rentas">Ver renta</Link>
                <Link to="/rentas/agregar_renta">Agregar renta</Link>
                <Link to="/rentas/actualizar_renta">Actualizar renta</Link>
                <Link to="/">Regresar</Link>
            </div>
            <Outlet />
        </div>
    );
};

export default Rentas;