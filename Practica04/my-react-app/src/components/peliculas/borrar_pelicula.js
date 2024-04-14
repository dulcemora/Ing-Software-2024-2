import React, { useState } from 'react';

function Borrar_pelicula() {
  const [idPelicula, setIdPelicula] = useState('');

  const handleInputChange = (event) => {
    setIdPelicula(event.target.value);
  };

  const handleFormSubmit = (event) => {
    event.preventDefault();
    console.log('ID de la película a borrar:', idPelicula);
  };

  return (
    <div className="container">
      <h1>Borrar Película</h1>
      <div className="form-container">
        <form onSubmit={handleFormSubmit}>
          <label htmlFor="idPelicula">Ingrese el ID:</label>
          <input
            type="text"
            id="idPelicula"
            name="idPelicula"
            value={idPelicula}
            onChange={handleInputChange}
            required
          />
          <div className="button-container">
            <button type="submit">Eliminar Película</button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Borrar_pelicula;