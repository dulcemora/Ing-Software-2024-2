import React, { useState } from 'react';

function Agregar_cliente() {
  const [nombre, setNombre] = useState('');
  const [apPat, setApPat] = useState('');
  const [apMat, setApMat] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');

  const handleNombreChange = (event) => {
    setNombre(event.target.value);
  };

  const handleApPatChange = (event) => {
    setApPat(event.target.value);
  };

  const handleApMatChange = (event) => {
    setApMat(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handleFormSubmit = (event) => {
    event.preventDefault();
    console.log('Nombre:', nombre);
    console.log('Apellido Paterno:', apPat);
    console.log('Apellido Materno:', apMat);
    console.log('Contraseña:', password);
    console.log('Email:', email);;
  };

  return (
    <div className="container">
      <h1>Agregar cliente</h1>
      <div className="form-container">
        <form onSubmit={handleFormSubmit}>
          <label htmlFor="nombre">Ingrese el nombre:</label>
          <input type="text" id="nombre" name="nombre" value={nombre} onChange={handleNombreChange} required />
          <br />
          <label htmlFor="apPat">Ingrese el apellido paterno:</label>
          <input type="text" id="apPat" name="apPat" value={apPat} onChange={handleApPatChange} required />
          <br />
          <label htmlFor="apMat">Ingrese el apellido materno:</label>
          <input type="text" id="apMat" name="apMat" value={apMat} onChange={handleApMatChange} required />
          <br />
          <label htmlFor="password">Ingrese la contraseña:</label>
          <input type="password" id="password" name="password" value={password} onChange={handlePasswordChange} required />
          <br />
          <label htmlFor="email">Ingrese el email:</label>
          <input type="email" id="email" name="email" value={email} onChange={handleEmailChange} required />
          <br />
          <div className="button-container">
            <button type="submit">Agregar usuario</button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Agregar_cliente;