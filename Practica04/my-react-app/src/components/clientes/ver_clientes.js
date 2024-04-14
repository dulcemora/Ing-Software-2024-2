import React from "react";

const Ver_clientes = () => {
  const clientes = [
    { idCliente: 1, nombre: "Aldo", apPat: "Herrera", apMat: "Juarez", email: "aldito@example.com", telefono: "1234567890" },
    { idCliente: 2, nombre: "Mildred", apPat: "Calvillo", apMat: "Juarez", email: "millie11@example.com", telefono: "0456321987" },
    { idCliente: 3, nombre: "Alexia", apPat: "Ramirez", apMat: "Montes", email: "thv@example.com", telefono: "4560123987" },
    { idCliente: 4, nombre: "Julieta", apPat: "Hernandez", apMat: "Mora", email: "cliente4@example.com", telefono: "0123789456" },
    { idCliente: 5, nombre: "Omar", apPat: "Gomez", apMat: "Carranza", email: "cliente5@example.com", telefono: "0987654321" }
  ];

  return (
    <div className="Ver_clientes">
      <h2>Ver clientes</h2>
      <div className="table-container">
        <table>
          <thead>
            <tr>
              <th>ID Cliente</th>
              <th>Nombre</th>
              <th>Apellido Paterno</th>
              <th>Apellido Materno</th>
              <th>Email</th>
              <th>Teléfono</th>
            </tr>
          </thead>
          <tbody>
            {clientes.map(cliente => (
              <tr key={cliente.idCliente}>
                <td>{cliente.idCliente}</td>
                <td>{cliente.nombre}</td>
                <td>{cliente.apPat}</td>
                <td>{cliente.apMat}</td>
                <td>{cliente.email}</td>
                <td>{cliente.telefono}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Ver_clientes;
