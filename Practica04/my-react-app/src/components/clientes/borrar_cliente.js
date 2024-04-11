import React, { useState } from 'react';
import './borrar_cliente.css';

function borrar_cliente() {
  const [idUsuario, setIdUsuario] = useState('');

  const handleIdUsuarioChange = (event) => {
    setIdUsuario(event.target.value);
  };

  const handleFormSubmit = (event) => {
    event.preventDefault();
    console.log('ID de usuario a eliminar:', idUsuario);
  };

  return (
    <div className="container">
      <h1>Borrar Usuario</h1>
      <div className="form-container">
        <form onSubmit={handleFormSubmit}>
          <label htmlFor="idUsuario">Ingrese el ID:</label>
          <input type="text" id="idUsuario" name="idUsuario" value={idUsuario} onChange={handleIdUsuarioChange} />
          <br />
          <div className="button-container">
            <button type="submit">Eliminar usuario</button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default borrar_cliente;