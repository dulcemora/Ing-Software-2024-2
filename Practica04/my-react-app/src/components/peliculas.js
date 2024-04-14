import React from 'react';
//import './Peliculas.css';

function Peliculas() {
  return (
    <div className="container">
      <h1>Rentar</h1>
      <div className="buttons">
        <div className="button-group">
          <button onClick={() => window.location.href='/peliculas/ver_peliculas'}>Ver todas las peliculas</button>
        </div>
        <div className="button-group">
          <button onClick={() => window.location.href='/peliculas/actualizar_pelicula'}>Actualizar pelicula</button>
        </div>
        <div className="button-group">
          <button onClick={() => window.location.href='/peliculas/agregar_pelicula'}>Agregar pelicula</button>
        </div>
        <div className="button-group">
          <button onClick={() => window.location.href='/peliculas/borrar_pelicula'}>Borrar pelicula</button>
        </div>
        <div className="button-group">
          <button onClick={() => window.location.href='/'}>Regresar</button>
        </div>
      </div>
    </div>
  );
}

export default Peliculas;