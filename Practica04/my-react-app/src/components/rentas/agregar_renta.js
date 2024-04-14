import React from 'react';

function Agregar_renta() {
  return (
    <div className="container">
      <h1>Agregar renta</h1>
      <div className="form-container">
        <form action="/rentas/agregar_renta" method="POST">
          <label htmlFor="idCliente">ID Cliente:</label>
          <input type="text" id="idCliente" name="idCliente" required />
          <br />
          <label htmlFor="idPelicula">ID Pelicula:</label>
          <input type="text" id="idPelicula" name="idPelicula" required />
          <br />
          <label htmlFor="fecha_renta">Fecha de Renta:</label>
          <input type="date" id="fecha_renta" name="fecha_renta" required />
          <br />
          <label htmlFor="dias_de_renta">Dias de Renta:</label>
          <input type="number" id="dias_de_renta" name="dias_de_renta" required />
          <br />
          <div className="button-container">
            <button type="submit">Agregar renta</button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Agregar_renta;