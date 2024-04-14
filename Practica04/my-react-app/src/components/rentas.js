import React from 'react';
import { Link } from 'react-router-dom';
import Ver_rentas from "./renta/ver_rentas";
import Actualizar_renta from "./renta/actualizar_renta";
import Agregar_renta from "./renta/agregar_renta";

function Rentas() {
  return (
    <div className="container">
      <h1>Rentar</h1>
      <div className="buttons">
        <div className="button-group">
          <Link to="renta/ver_rentas"><button>Ver todas las rentas</button></Link>
        </div>
        <div className="button-group">
          <Link to="renta/actualizar_renta"><button>Actualizar renta</button></Link>
        </div>
        <div className="button-group">
          <Link to="renta/agregar_renta"><button>Agregar renta</button></Link>
        </div>
        <div className="button-group">
          <Link to="/"><button>Regresar</button></Link>
        </div>
      </div>
    </div>
  );
}

export default Rentas;
