import 'bootstrap/dist/css/bootstrap.min.css';
import React, { useState, useEffect } from "react";
import './App.css';
import NavBar from './Components/NavBar';
import Carrusel from './Components/Carousel';
import NavBar2 from './Components/NavBar2';
import Reglamento from './Components/Reglamento';
function App() {
  return (
    <>
    <NavBar2/>
    <Carrusel/>

    <h1>NOVEDADES</h1>
    <p4>Nada aun :)</p4>
    <Reglamento/>
    </>
  );
}

export default App;

