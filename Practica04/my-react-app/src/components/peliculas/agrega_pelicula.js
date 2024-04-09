import React from 'react';
import './agrega_pelicula.css';

function agrega_pelicula() {
  return (
    <div className="container">
      <h1>Agregar película</h1>
      <div className="form-container">
        <form action="/pelicula/agregar_pelicula" method="POST">
          <label htmlFor="nombre">Nombre:</label>
          <input type="text" id="nombre" name="nombre" required />
          <br />
          <label htmlFor="genero">Género:</label>
          <input type="text" id="genero" name="genero" required />
          <br />
          <label htmlFor="duracion">Duración:</label>
          <input type="number" id="duracion" name="duracion" required />
          <br />
          <label htmlFor="inventario">Inventario:</label>
          <input type="number" id="inventario" name="inventario" required />
          <br />
          <div className="button-container">
            <button type="submit">Crear película</button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default agrega_pelicula;
