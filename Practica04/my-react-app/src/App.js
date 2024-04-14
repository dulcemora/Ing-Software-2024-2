import React, { Component } from "react";
import {
    BrowserRouter as Router,
    Routes,
    Route,
    Link,
} from "react-router-dom";
import Home from "./components/home";
import Clientes from "./components/clientes";
import Peliculas from "./components/peliculas";
import Rentas from "./components/rentas";
import "./App.css";

class App extends Component {
    render() {
        return (
            <Router>
                <div className="App">
                    <ul className="App-header">
                        <li>
                            <Link to="/">Home</Link>
                        </li>
                        <li>
                            <Link to="/clientes">
                                Clientes
                            </Link>
                        </li>
                        <li>
                            <Link to="/peliculas">
                                Peliculas
                            </Link>
                        </li>
                        <li>
                            <Link to="/rentas">
                                Rentas
                            </Link>
                        </li>
                    </ul>
                    <Routes>
                        <Route
                            path="/"
                            element={<Home />}
                        ></Route>
                        <Route
                            path="/clientes"
                            element={<Clientes />}
                        ></Route>
                        <Route
                            path="/peliculas"
                            element={<Peliculas />}
                        ></Route>
                        <Route
                            path="/rentas"
                            element={<Rentas />}
                        ></Route>
                    </Routes>
                </div>
            </Router>
        );
    }
}

export default App;