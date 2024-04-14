import React from 'react';

function Ver_clientes({ clientes }) {
  return (
    <div className="container">
      <h1>Clientes</h1>
      <div className="table-container">
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Nombre</th>
              <th>Apellido Paterno</th>
              <th>Apellido Materno</th>
              <th>Password</th>
              <th>Email</th>
              <th>Profile Picture</th>
              <th>SuperUser</th>
            </tr>
          </thead>
          <tbody>
            {clientes.map((cliente, index) => (
              <tr key={index}>
                <td>{cliente.idUsuario}</td>
                <td>{cliente.nombre}</td>
                <td>{cliente.apPat}</td>
                <td>{cliente.apMat}</td>
                <td>{cliente.password}</td>
                <td>{cliente.email}</td>
                <td>{cliente.profilePicture}</td>
                <td>{cliente.superUser}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Ver_clientes;
