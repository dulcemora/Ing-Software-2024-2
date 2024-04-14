import React from 'react';
import { Link } from 'react-router-dom';
import Ver_clientes from "./clientes/ver_clientes";
import Actualizar_cliente from "./clientes/actualizar_cliente";
import Agregar_cliente from "./clientes/agregar_cliente";
import Borrar_clientes from "./clientes/borrar_cliente";

function Clientes() {
  return (
    <div className="container">
      <h1>Peliculas</h1>
      <div className="buttons">
        <div className="button-group">
          <Link to="clientes/ver_clientes"><button>Ver todos los clientes</button></Link>
        </div>
        <div className="button-group">
          <Link to="clientes/actualizar_cliente"><button>Actualizar clientes</button></Link>
        </div>
        <div className="button-group">
          <Link to="clientes/agregar_cliente"><button>Agregar clientes</button></Link>
        </div>
        <div className="button-group">
          <Link to="clientes/borrar_cliente"><button>Borrar clientes</button></Link>
        </div>
        <div className="button-group">
          <Link to="/"><button>Regresar</button></Link>
        </div>
      </div>
    </div>
  );
}

export default Clientes;