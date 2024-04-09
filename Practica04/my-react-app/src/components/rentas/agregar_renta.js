import React from 'react';
import './agregar_renta.css';

function agregar_renta({ usuarios, peliculas }) {
  return (
    <div className="container">
      <h1>Agregar renta</h1>
      <div className="form-container">
        <form action="/rentar/agregar_renta" method="POST">
          <label htmlFor="idUsuario">ID Usuario:</label>
          <select id="idUsuario" name="idUsuario" required>
            {usuarios.map((usuario, index) => (
              <option key={index} value={usuario.idUsuario}>{usuario.idUsuario}</option>
            ))}
          </select>
          <br />
          <label htmlFor="idPelicula">ID Película:</label>
          <select id="idPelicula" name="idPelicula" required>
            {peliculas.map((pelicula, index) => (
              <option key={index} value={pelicula.idPelicula}>{pelicula.idPelicula}</option>
            ))}
          </select>
          <br />
          <label htmlFor="fecha_renta">Fecha de Renta:</label>
          <input type="date" id="fecha_renta" name="fecha_renta" required />
          <label htmlFor="dias_de_renta">Días de Renta:</label>
          <input type="number" id="dias_de_renta" name="dias_de_renta" required />
          <div className="button-container">
            <button type="submit">Agregar Renta</button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default agregar_renta;
