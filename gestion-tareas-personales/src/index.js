import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
// Se renderiza el componente "App" dentro del elemento con id "root", 
// en el modo estricto de React; esto para detectar problemas dentro de la aplicacion.
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
