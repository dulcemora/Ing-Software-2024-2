import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

/*
function index() {
  return (
    <div style={{ margin: '0 auto', width: '200px', textAlign: 'center' }}>
      <h1>Clonbuster</h1>
      <div style={{ margin: '0 auto', width: '200px' }}>
        <button onClick={() => window.location.href='/clientes'}>Clientes</button>
        <button onClick={() => window.location.href='/peliculas'}>Peliculas</button>
        <button onClick={() => window.location.href='/rentas'}>Rentar</button>
      </div>
    </div>
  );
}
*/

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

export default index;
