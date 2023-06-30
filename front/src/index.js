import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import Alumno from "./Paginas/Pag_alumno";
import Profe from "./Paginas/Pag_profes"
import Admin from "./Paginas/Pag_admin"



const router = createBrowserRouter([
  {
    path: "/",
    element: <App/>,
  },
  {
    path: "Alumno",
    element: <Alumno/>,
  },
  {
    path: "Profe",
    element: <Profe/>,
  },
  {
    path: "Admin",
    element: <Admin/>,
  },
  {
    path: "App",
    element: <App/>,
  },
]);



const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router = {router} />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
