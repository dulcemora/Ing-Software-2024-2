import React from 'react';
import './ver_rentas.css';

function actualizar_renta({ renta }) {
  const handleFormSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const rentado = formData.get('rentado');
    console.log('Rentado:', rentado);
  };

  return (
    <div className="container">
      <h1>Actualizar Renta</h1>
      <div className="form-container">
        <form onSubmit={handleFormSubmit}>
          <label htmlFor="rentado_true">Rentado:</label>
          <input type="radio" id="rentado_true" name="rentado" value="True" defaultChecked={renta.rentado} />
          <label htmlFor="rentado_true">True</label>
          <input type="radio" id="rentado_false" name="rentado" value="False" defaultChecked={!renta.rentado} />
          <label htmlFor="rentado_false">False</label>
          <br />
          <div className="button-container">
            <button type="submit">Actualizar Estatus</button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default actualizar_renta;
