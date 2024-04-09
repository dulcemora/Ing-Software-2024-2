import React from 'react';
import './Rentas.css';

function Rentas() {
  return (
    <div className="container">
      <h1>Rentar</h1>
      <div className="buttons">
        <div className="button-group">
          <button onClick={() => window.location.href='/rentas/ver_rentas'}>Ver todas las rentas</button>
        </div>
        <div className="button-group">
          <button onClick={() => window.location.href='/rentas/actualizar_renta'}>Actualizar renta</button>
        </div>
        <div className="button-group">
          <button onClick={() => window.location.href='/rentas/agregar_renta'}>Agregar renta</button>
        </div>
        <div className="button-group">
          <button onClick={() => window.location.href='/'}>Regresar</button>
        </div>
      </div>
    </div>
  );
}

export default Rentas;