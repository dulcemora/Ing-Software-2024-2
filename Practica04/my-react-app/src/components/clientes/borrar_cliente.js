import React from 'react';

function borrar_cliente({ todos, borrar_cliente }) {
  return (
    <div className="borrar-cliente">
      <h2>Borrar Cliente</h2>
      <ul>
        {todos.map(todo => (
          <li key={todo.id} className="borra-cliente">
            <span>{todo.text}</span>
            <button onClick={() => borrar_cliente(todo.id)}>Eliminar</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default borrar_cliente;