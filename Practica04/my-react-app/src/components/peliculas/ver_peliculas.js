import React from "react";

const Ver_peliculas = () => {
  // Genera datos de películas aleatorias
  const peliculas = [
    { idPelicula: 1, nombre: "Kung Fu Panda 4", genero: "Comedia", duracion: "94 min", inventario: 20 },
    { idPelicula: 2, nombre: "Robot Dreams", genero: "Musical", duracion: "102 min", inventario: 10 },
    { idPelicula: 3, nombre: "Your Name", genero: "Fantasia/Romance", duracion: "107 min", inventario: 12 },
    { idPelicula: 4, nombre: "Orgullo y Prejuicio", genero: "Romance", duracion: "127 min", inventario: 7 },
    { idPelicula: 5, nombre: "El tiempo contigo", genero: "Fantasia", duracion: "114 min", inventario: 18 }
  ];

  return (
    <div className="Ver_peliculas">
      <h2>Ver películas</h2>
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
            {peliculas.map(pelicula => (
              <tr key={pelicula.idPelicula}>
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
};

export default Ver_peliculas;
