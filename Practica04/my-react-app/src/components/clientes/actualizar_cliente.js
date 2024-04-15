import React, { useState } from 'react';

function Actualizar_cliente() {
  const [idUsuario, setIdUsuario] = useState('');
  const [campoActualizar, setCampoActualizar] = useState('nombre');
  const [nuevoValor, setNuevoValor] = useState('');

  const handleIdUsuarioChange = (event) => {
    setIdUsuario(event.target.value);
  };

  const handleCampoActualizarChange = (event) => {
    setCampoActualizar(event.target.value);
  };

  const handleNuevoValorChange = (event) => {
    setNuevoValor(event.target.value);
  };

  const handleFormSubmit = (event) => {
    event.preventDefault();
    console.log('ID de usuario:', idUsuario);
    console.log('Campo a actualizar:', campoActualizar);
    console.log('Nuevo valor:', nuevoValor);
  };

  return (
    <div className="container">
      <h1>Actualizar cliente</h1>
      <div className="form-container">
        <form onSubmit={handleFormSubmit}>
          <label htmlFor="idUsuario">ID de Usuario:</label>
          <input type="text" id="idUsuario" name="idUsuario" value={idUsuario} onChange={handleIdUsuarioChange} />
          <br />
          <label htmlFor="campoActualizar">Campo a Actualizar:</label>
          <select id="campoActualizar" name="campoActualizar" value={campoActualizar} onChange={handleCampoActualizarChange}>
            <option value="nombre">Nombre</option>
            <option value="apPat">Apellido Paterno</option>
            <option value="apMat">Apellido Materno</option>
            <option value="password">Password</option>
            <option value="email">Email</option>
          </select>
          <br />
          <label htmlFor="nuevoValor">Nuevo Valor:</label>
          <input type="text" id="nuevoValor" name="nuevoValor" value={nuevoValor} onChange={handleNuevoValorChange} />
          <br />
          <div className="button-container">
            <button type="submit">Actualizar Usuario</button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Actualizar_cliente;