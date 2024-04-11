import React from 'react';
import './App.css';
//import AgregarUsuario from './AgregarUsuario';
//import BorrarUsuario from './BorrarUsuario';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Bienvenido a Clonbuster</h1>
        <div style={{ margin: '0 auto', width: '200px', textAlign: 'center' }}>
          <h1>Clonbuster</h1>
          <div style={{ margin: '0 auto', width: '200px' }}>
            <button onClick={() => window.location.href='/clientes'}>Clientes</button>
            <button onClick={() => window.location.href='/peliculas'}>Peliculas</button>
            <button onClick={() => window.location.href='/rentas'}>Rentar</button>
          </div>
        </div>
      </header>
    </div>
  );
}

export default App;