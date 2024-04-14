import React from 'react';

function Ver_peliculas({ peliculas }) {
  return (
    <div className="container">
      <h1>Peliculas</h1>
      <div className="table-container">
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Nombre</th>
              <th>Género</th>
              <th>Duración</th>
              <th>Inventario</th>
            </tr>
          </thead>
          <tbody>
            {peliculas.map((pelicula, index) => (
              <tr key={index}>
                <td>{pelicula.idPelicula}</td>
                <td>{pelicula.nombre}</td>
                <td>{pelicula.genero}</td>
                <td>{pelicula.duracion}</td>
                <td>{pelicula.inventario}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Ver_peliculas;