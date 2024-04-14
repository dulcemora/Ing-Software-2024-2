import React from "react";
import { Link, Outlet } from "react-router-dom";
import "./clientes.css"; 

const Clientes = () => {
    return (
        <div className="Clientes">
            <h1>Clientes</h1>
            <div className="clientes-nav">
                <Link to="/clientes/ver_clientes">Ver clientes</Link>
                <Link to="/clientes/agregar_cliente">Agregar cliente</Link>
                <Link to="/clientes/actualizar_cliente">Actualizar cliente</Link>
                <Link to="/clientes/actualizar_cliente">Borrar cliente</Link>
                <Link to="/">Regresar</Link>
            </div>
            <Outlet />
        </div>
    );
};

export default Clientes;