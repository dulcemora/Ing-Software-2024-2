import React, { useState } from 'react';

function Actualizar_pelicula() {
  const [idPelicula, setIdPelicula] = useState('');
  const [campoActualizar, setCampoActualizar] = useState('nombre');
  const [nuevoValor, setNuevoValor] = useState('');

  const handleIdPeliculaChange = (event) => {
    setIdPelicula(event.target.value);
  };

  const handleCampoActualizarChange = (event) => {
    setCampoActualizar(event.target.value);
  };

  const handleNuevoValorChange = (event) => {
    setNuevoValor(event.target.value);
  };

  const handleFormSubmit = (event) => {
    event.preventDefault();
    console.log('ID de la película:', idPelicula);
    console.log('Campo a actualizar:', campoActualizar);
    console.log('Nuevo valor:', nuevoValor);
  };

  return (
    <div className="container">
      <h1>Actualizar Película</h1>
      <div className="form-container">
        <form onSubmit={handleFormSubmit}>
          <label htmlFor="idPelicula">ID:</label>
          <input type="text" id="idPelicula" name="idPelicula" value={idPelicula} onChange={handleIdPeliculaChange} />
          <br />
          <label htmlFor="campoActualizar">Campo a Actualizar:</label>
          <select id="campoActualizar" name="campoActualizar" value={campoActualizar} onChange={handleCampoActualizarChange}>
            <option value="nombre">Nombre</option>
            <option value="genero">Género</option>
            <option value="duracion">Duración</option>
            <option value="inventario">Inventario</option>
          </select>
          <br />
          <label htmlFor="nuevoValor">Nuevo Valor:</label>
          <input type="text" id="nuevoValor" name="nuevoValor" value={nuevoValor} onChange={handleNuevoValorChange} />
          <br />
          <div className="button-container">
            <button type="submit">Actualizar Película</button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Actualizar_pelicula;