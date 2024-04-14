import React from 'react';
//import './Clientes.css';

function Clientes() {
  return (
    <div className="container">
      <h1>Clientes</h1>
      <div className="buttons">
        <div className="button-group">
          <button onClick={() => window.location.href='/clientes/ver_clientes'}>Ver todas las clientes</button>
        </div>
        <div className="button-group">
          <button onClick={() => window.location.href='/clientes/actualizar_cliente'}>Actualizar cliente</button>
        </div>
        <div className="button-group">
          <button onClick={() => window.location.href='/clientes/agregar_cliente'}>Agregar cliente</button>
        </div>
        <div className="button-group">
          <button onClick={() => window.location.href='/clientes/borrar_cliente'}>Borrar cliente</button>
        </div>
        <div className="button-group">
          <button onClick={() => window.location.href='/'}>Regresar</button>
        </div>
      </div>
    </div>
  );
}

export default Clientes;