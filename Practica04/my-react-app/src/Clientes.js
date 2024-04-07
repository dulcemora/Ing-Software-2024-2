import React, { useState } from 'react';
import TodoList from './components/TodoList';
import agrega_cliente from './components/agrega_cliente';
import './Clientes.css';

function Clientes() {
  const [todos, setTodos] = useState([]);

  const agrega_cliente = (text) => {
    const newTodo = {
      id: Date.now(),
      text: text
    };
    setTodos([...todos, newTodo]);
  };

  const deleteTodo = (id) => {
    setTodos(todos.filter(todo => todo.id !== id));
  };

  return (
    <div className="container">
      <h1>Clientes</h1>
      <agrega_cliente agrega_cliente={agrega_cliente} />
      <TodoList todos={todos} deleteTodo={deleteTodo} />
    </div>
  );
}

export default Clientes;