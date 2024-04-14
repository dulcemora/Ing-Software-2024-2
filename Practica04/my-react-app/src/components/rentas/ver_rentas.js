import React from "react";

const Ver_rentas = () => {
  // Genera datos de rentas aleatorias
  const rentas = [
    { idRenta: 1, idCliente: 5, idPelicula: 1, fechaRenta: "2024-04-04", dias_de_renta: "10" },
    { idRenta: 2, idCliente: 2, idPelicula: 2, fechaRenta: "2024-04-02", dias_de_renta: "12" },
    { idRenta: 3, idCliente: 3, idPelicula: 2, fechaRenta: "2024-03-30", dias_de_renta: "15" },
    { idRenta: 4, idCliente: 5, idPelicula: 2, fechaRenta: "2024-04-05", dias_de_renta: "9" },
    { idRenta: 5, idCliente: 5, idPelicula: 5, fechaRenta: "2024-04-01", dias_de_renta: "14" }
  ];

  return (
    <div className="Ver_rentas">
      <h2>Ver rentas</h2>
      <div className="table-container">
        <table>
          <thead>
            <tr>
              <th>ID Renta</th>
              <th>ID Cliente</th>
              <th>ID Película</th>
              <th>Fecha Renta</th>
              <th>Dias de Renta</th>
            </tr>
          </thead>
          <tbody>
            {rentas.map(renta => (
              <tr key={renta.idRenta}>
                <td>{renta.idRenta}</td>
                <td>{renta.idCliente}</td>
                <td>{renta.idPelicula}</td>
                <td>{renta.fechaRenta}</td>
                <td>{renta.dias_de_renta}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Ver_rentas;