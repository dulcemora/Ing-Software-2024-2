import React, { useState } from 'react';

function agrega_cliente({ agrega_cliente }) {
  const [text, setText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!text.trim()) return;
    agrega_cliente(text);
    setText('');
  };

  return (
    <div className="agrega-cliente">
      <h2>Agregar Cliente</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" value={text} onChange={(e) => setText(e.target.value)} />
        <button type="submit">Agregar</button>
      </form>
    </div>
  );
}

export default agrega_cliente;