import React from 'react';

function Actualizar_renta() {
  return (
    <div className="container">
      <h1>Actualizar renta</h1>
      <div className="form-container">
        <form action="/rentas/actualizar_renta" method="POST">
          <label htmlFor="estatus">Estatus:</label>
          <input type="radio" id="estatus" name="estatus" required />
          <br />
          <div className="button-container">
            <button type="submit">Actualizar renta</button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Actualizar_renta;