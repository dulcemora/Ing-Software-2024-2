import React from 'react';
import './ver_rentas.css';

function ver_rentas({ rentas }) {
  return (
    <div className="container">
      <h1>Rentas</h1>
      <div className="table-container">
        <table>
          <thead>
            <tr>
              <th>ID Rentar</th>
              <th>ID Usuario</th>
              <th>ID Pelicula</th>
              <th>Fecha Renta</th>
              <th>Dias De Renta</th>
              <th>Estatus</th>
            </tr>
          </thead>
          <tbody>
            {rentas.map((renta, index) => (
              <tr key={index}>
                <td>{renta.idRentar}</td>
                <td>{renta.usuario.idUsuario}</td>
                <td>{renta.pelicula.idPelicula}</td>
                <td>{renta.fecha_renta}</td>
                <td>{renta.dias_de_renta}</td>
                <td>{renta.estatus}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default ver_rentas;
