import React from 'react';
import { Link } from 'react-router-dom';
import Ver_peliculas from "./peliculas/ver_peliculas";
import Actualizar_pelicula from "./peliculas/actualizar_pelicula";
import Agregar_pelicula from "./peliculas/agregar_pelicula";
import Borrar_pelicula from "./peliculas/borrar_pelicula";

function Peliculas() {
  return (
    <div className="container">
      <h1>Peliculas</h1>
      <div className="buttons">
        <div className="button-group">
          <Link to="peliculas/ver_peliculas"><button>Ver todas las peliculas</button></Link>
        </div>
        <div className="button-group">
          <Link to="peliculas/actualizar_pelicula"><button>Actualizar pelicula</button></Link>
        </div>
        <div className="button-group">
          <Link to="peliculas/agregar_pelicula"><button>Agregar pelicula</button></Link>
        </div>
        <div className="button-group">
          <Link to="peliculas/borrar_pelicula"><button>Borrar pelicula</button></Link>
        </div>
        <div className="button-group">
          <Link to="/"><button>Regresar</button></Link>
        </div>
      </div>
    </div>
  );
}

export default Peliculas;